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
tgex_script="/usr/bin/python3 /staging/Tgex/tgex_uploadSamples.py --config /staging/Tgex/tgex.config.yml"
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
#########################################################get tgex parameter
str_wes,str_wgs="",""
wes_vcf,wgs_vcf="",""
if args.wes:
    wes_vcf=out_path+"/wes_vcf"
    subprocess.check_call("mkdir -p %s"%(wes_vcf),shell=True)
    str_wes=core.parse_samplelist.run(args.wes)

if args.wgs:
    wgs_vcf=out_path+"/wgs_vcf"
    subprocess.check_call("mkdir -p %s"%(wgs_vcf),shell=True)
    str_wgs = core.parse_samplelist.run(args.wgs)
#########################################################fastq2vcf
sample_name,file2="",""
for(root, dirs, files) in os.walk(fastq_dir):
    for file in files:
        if re.search(r'_R1_', file):
            array = file.split("_")
            for i in range(0, len(array) - 3):
                sample_name += array[i]
                sample_name += "_"
            sample_name = sample_name.strip("_")
            file2 = file.replace("_R1_", "_R2_")
            if sample_name in str_wes:
                subprocess.check_call("mkdir -p %s/%s" % (wes_vcf, sample_name), shell=True)
                if args.normal_wes:
                    core.wes_PoN.run(args.ref,file,file2,"%s/%s"%(wes_vcf,sample_name),sample_name,args.bed,args.normal_wes)
                else:
                    core.wes.run(args.ref, file, file2, "%s/%s" % (wes_vcf, sample_name), sample_name,args.bed)
                if sample_name!=str_wes[sample_name]:
                    tgex_script+=" %s "%(str_wes[sample_name])
                    tgex_script+=" --snvVcf %s/%s/%s.hard-filtered.vcf.gz --cnvVcf %s/%s/%s.cnv.vcf.gz --svVcf %s/%s/%s.sv.vcf.gz "%(wes_vcf,sample_name,sample_name,wes_vcf,sample_name,sample_name,wes_vcf,sample_name,sample_name)
                    subprocess.check_call(tgex_script, shell=True)
            if sample_name in str_wgs:
                subprocess.check_call("mkdir -p %s/%s" % (wgs_vcf, sample_name), shell=True)
                if args.normal_wgs:
                    core.wgs_PoN.run(args.ref,file,file2,"%s/%s"%(wgs_vcf, sample_name),sample_name,args.normal_wgs)
                else:
                    core.wgs.run(args.ref,file,file2,"%s/%s"%(wgs_vcf, sample_name),sample_name)
                if sample_name!=str_wgs[sample_name]:
                    tgex_script += " %s " % (str_wgs[sample_name])
                    tgex_script += " --snvVcf %s/%s/%s.hard-filtered.vcf.gz --cnvVcf %s/%s/%s.cnv.vcf.gz --svVcf %s/%s/%s.sv.vcf.gz "%(wgs_vcf,sample_name,sample_name,wgs_vcf,sample_name,sample_name,wgs_vcf,sample_name,sample_name)
                    subprocess.check_call(tgex_script,shell=True)
#########################################################
if args.wes:
    core.result_parse.run(wes_vcf,"%s.wes"%(localtime),args.outdir)
if args.wgs:
    core.result_parse.run(wgs_vcf,"%s.wgs"%(localtime),args.outdir)
