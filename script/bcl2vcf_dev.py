#Email:yucai.fan@illumina.com
#2020.11.16 version:1.0
#2020.11.30 version:2.0 fix bug:the samplesheet in '--no-lane-splitting'
#2021.01.03 version:3.0 rewrite+tgex+PoN

import os,sys,re,argparse,time,subprocess
sub=os.path.abspath(__file__)
dir_name=os.path.dirname(sub)
sys.path.append(dir_name)
import core

parser=argparse.ArgumentParser("This script run from bcl to vcf.\n\n")
parser.add_argument("-i","--indir",help="bcl directory must be given(force)",required=True)
parser.add_argument("-s","--samplesheet",help="sample sheet must be given(force)",required=True)
parser.add_argument("-r","--ref",help="reference directory must be given(force)",required=True)
parser.add_argument("-e","--wes",help="exon sample list")
parser.add_argument("-b","--bed",help="bed file")
parser.add_argument("-g","--wgs",help="wgs sample list")
parser.add_argument("-o","--outdir",help="output directory")
parser.add_argument("-ne","--normal_wes",help="exon normal list file")
parser.add_argument("-nw","--normal_wgs",help="wgs normal list file")
args=parser.parse_args()
##########################################################check once again
python3 = subprocess.getoutput('which python3')
if not re.search('python3',python3):
    print("Not find python3,you should set the python3 directory in %s 24 line"%(sys.argv[0]))
##########################################################
if not args.wes and not args.wgs:
    print("Erro:You must defined wes_sample.list or wgs_sample.list\n\n")
    exit()
if args.wes and not args.bed:
    print("Erro:bed file must be given\n\n")
    exit()
if not args.ref:
    print("Erro:reference directory must be given\n\n")
    exit()
#########################################################check output directory
localtime = time.strftime("%Y-%m-%d", time.localtime())
out_path=""
if not args.outdir:
    out_path=os.getcwd()+"/"+localtime
    subprocess.check_call("mkdir -p %s"%(out_path),shell=True)
else:
    out_path=os.path.abspath(args.outdir)
fastq_dir=out_path+"/fastq"
subprocess.check_call("mkdir -p %s"%(fastq_dir),shell=True)
#########################################################run bcl2fastq
core.bcl2fastq.run(args.samplesheet,args.indir,fastq_dir)
#########################################################parse sample list and mkdir wes/wgs vcf output directory
fastq2vcf_wes_par,fastq2vcf_wgs_par,wes_vcf,wgs_vcf={},{},"",""
if args.wes:
    fastq2vcf_wes_par=core.parse_samplelist.run(args.wes)
    wes_vcf = out_path + "/wes_vcf"
    subprocess.check_call("mkdir -p %s" % (wes_vcf), shell=True)
if args.wgs:
    wgs_vcf = out_path + "/wgs_vcf"
    subprocess.check_call("mkdir -p %s" % (wgs_vcf), shell=True)
    fastq2vcf_wgs_par=core.parse_samplelist.run(args.wgs)
#########################################################run fastq2vcf
for(root, dirs, files) in os.walk(fastq_dir):
    for file in files:
        if re.search(".fastq.gz$",file) and re.search('_R1_',file):
            R1=os.path.join(root,file)
            R2=R1.replace("_R1_","_R2_")
            for sample_name in fastq2vcf_wes_par:
                if re.search(sample_name,R1) and not os.path.exists("%s/%s/%s.time_metrics.csv"%(wes_vcf,sample_name,sample_name)):
                    if args.normal_wes:
                        core.wes_PoN.run(args.ref,R1,R2,"%s/%s"%(wes_vcf,sample_name),sample_name,args.bed,args.normal_wes)
                    else:
                        core.wes.run(args.ref,R1,R2,"%s/%s"%(wes_vcf,sample_name),sample_name,args.bed)
            for sample_name in fastq2vcf_wgs_par:
                if re.search(sample_name, R1) and not os.path.exists("%s/%s/%s.time_metrics.csv"%(wgs_vcf,sample_name,sample_name)):
                    if args.normal_wgs:
                        core.wgs_PoN.run(args.ref, R1, R2, "%s/%s"%(wgs_vcf,sample_name), sample_name,args.normal_wgs)
                    else:
                        core.wgs.run(args.ref, R1, R2, "%s/%s"%(wgs_vcf,sample_name), sample_name)
#########################################################
if args.wes:
    core.result_parse.run(wes_vcf,"%s.wes"%(localtime),out_path)#output total matrix
    core.copy2vcf.run(wes_vcf,"%s/combine_wes_vcf/"%(out_path))#copy pass vcf to one directoy
    ##############################################################maybe run tgex
    for sample_name in fastq2vcf_wes_par:
        if fastq2vcf_wes_par[sample_name]!="false":
            tgex_script = "%s %s/Tgex/tgex_uploadSamples.py --config %s/Tgex/tgex.config.yml " % (python3, dir_name, dir_name)
            for (root,dirs,files) in os.walk("%s/combine_wes_vcf/"%(out_path)):
                for file in files:
                    if re.search(sample_name,file):
                        if re.search('.sv.pass.vcf.gz$',file):
                            tgex_script+=" --svVcf %s "%(os.path.join(root,file))
                        if re.search('.hard-filtered.pass.vcf.gz$',file):
                            tgex_script+=" --snvVcf %s "%(os.path.join(root,file))
                        if re.search('.cnv.pass.vcf.gz$',file):
                            tgex_script+=" --cnvVcf %s "%(os.path.join(root,file))
                        print(tgex_script)
                        subprocess.check_call(tgex_script, shell=True)
if args.wgs:
    core.result_parse.run(wgs_vcf,"%s.wgs"%(localtime),out_path)#output total matri
    core.copy2vcf.run(wgs_vcf, "%s/combine_wgs_vcf/" % (out_path))#copy pass vcf to one directoy
    #########################################################maybe run tgex
    for sample_name in fastq2vcf_wgs_par:
        if fastq2vcf_wgs_par[sample_name] != "false":
            tgex_script = "%s %s/Tgex/tgex_uploadSamples.py --config %s/Tgex/tgex.config.yml " % (python3, dir_name, dir_name)
            for (root, dirs, files) in os.walk("%s/combine_wgs_vcf/" % (out_path)):
                for file in files:
                    if re.search(sample_name, file):
                        if re.search('.sv.pass.vcf.gz$', file):
                            tgex_script += " --svVcf %s " % (os.path.join(root, file))
                        if re.search('.hard-filtered.pass.vcf.gz$', file):
                            tgex_script += " --snvVcf %s " % (os.path.join(root, file))
                        if re.search('.cnv.pass.vcf.gz$', file):
                            tgex_script += " --cnvVcf %s " % (os.path.join(root, file))
                        print(tgex_script)
                        subprocess.check_call(tgex_script,shell=True)
#########################################################
print("Done")
