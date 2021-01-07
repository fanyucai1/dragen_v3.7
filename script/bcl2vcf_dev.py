#Email:yucai.fan@illumina.com
#2021.01.06

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
parser.add_argument("-ne","--normal_wes",help="exon normal list file",default="false")
parser.add_argument("-ng","--normal_wgs",help="wgs normal list file",default="false")
parser.add_argument("-c","--config",help="tgex config file",default="false")
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
    fastq2vcf_wes_par=core.run_tgex.run(args.wes)
    wes_vcf = out_path + "/wes_vcf"
    subprocess.check_call("mkdir -p %s" % (wes_vcf), shell=True)
    #fastq2vcf
    cmd='%s %s/germline_fastq2vcf.py -r %s -s % -o %s -f %s -p %s -b %s'%(python3,dir_name,args.ref,args.wes,wes_vcf, fastq_dir,args.normal_wes,args.bed)
    subprocess.check_call(cmd,shell=True)
    core.result_parse.run(wes_vcf, "%s.wes" % (localtime), out_path)  # output total matrix
    core.copy2vcf.run(wes_vcf, "%s/combine_wes_vcf/" % (out_path))  # copy pass vcf to one directoy
    if args.cofig!="false":
        core.run_tgex.run(args.wes,args.config,"%s/combine_wes_vcf/" % (out_path))
if args.wgs:
    wgs_vcf = out_path + "/wgs_vcf"
    subprocess.check_call("mkdir -p %s" % (wgs_vcf), shell=True)
    # fastq2vcf
    cmd = '%s %s/germline_fastq2vcf.py -r %s -s % -o %s -f %s -p %s' % (python3, dir_name, args.ref, args.wgs, wgs_vcf, fastq_dir, args.normal_wgs)
    subprocess.check_call(cmd, shell=True)
    core.result_parse.run(wgs_vcf, "%s.wgs" % (localtime), out_path)  # output total matrix
    core.copy2vcf.run(wgs_vcf, "%s/combine_wgs_vcf/" % (out_path))  # copy pass vcf to one directoy
    if args.cofig != "false":
        core.run_tgex.run(args.wgs, args.config, "%s/combine_wgs_vcf/" % (out_path))
#########################################################
print("Done")