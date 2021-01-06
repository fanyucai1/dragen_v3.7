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
#########################################################run fastq2vcf
