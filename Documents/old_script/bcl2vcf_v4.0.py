#Email:yucai.fan@illumina.com
#2020.11.16 version:1.0
#2020.11.30 version:2.0 fix bug:the samplesheet in '--no-lane-splitting'
#2021.01.04 vserion:3.0 fix bug:add parameter '--sample_name_suffix'
#2021.01.22 version:4.0 fix bug:add parameter '--PoN'

import os
import argparse
import time
import subprocess
import re

parser=argparse.ArgumentParser("This script run from bcl to vcf.\n\n")
parser.add_argument("-i","--indir",help="bcl directory must be given(force)",required=True)
parser.add_argument("-s","--samplesheet",help="sample sheet must be given(force)",required=True)
parser.add_argument("-r","--ref",help="reference directory must be given(force)",required=True)
parser.add_argument("-e","--wes",help="exon sample list")
parser.add_argument("-b","--bed",help="bed file")
parser.add_argument("-g","--wgs",help="wgs sample list")
parser.add_argument("-o","--outdir",help="output directory")
parser.add_argument("-p","--PoN",help="PoN file",default="false")
args=parser.parse_args()
##########################################################check once again
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
#########################################################identify samplesheet
infile=open(args.samplesheet,"r")
par,sample_name_suffix="",3
for line in infile:
    line=line.strip()
    if re.search('Sample_ID',line) or re.search('Sample_Name',line):
        if re.search('Lane',line):
            par=" --no-lane-splitting false "
            sample_name_suffix=4
        else:
            par = " --no-lane-splitting true "
infile.close()
#########################################################run bcl2fastq
command="dragen -f --bcl-conversion-only true --bcl-input-directory %s --output-directory %s --sample-sheet %s %s "%(os.path.abspath(args.indir),fastq_dir,os.path.abspath(args.samplesheet),par)
if not os.path.exists("%s/Logs/FastqComplete.txt"%(fastq_dir)):
    subprocess.check_call(command,shell=True)
    print("bcl2fastq finished\n")
#########################################################get sample name
wes_vcf,wgs_vcf,sample_wes,sample_wgs="","",[],[]
if args.wes:
    wes_vcf=out_path+"/wes_vcf"
    subprocess.check_call("mkdir -p %s"%(wes_vcf),shell=True)
    infile=open(args.wes,"r")
    for line in infile:
        sample_wes.append(line.strip())
    infile.close()

if args.wgs:
    wgs_vcf=out_path+"/wgs_vcf"
    subprocess.check_call("mkdir -p %s"%(wgs_vcf),shell=True)
    infile=open(args.wgs,"r")
    for line in infile:
        sample_wgs.append(line.strip())
    infile.close()
###########################################################print wes or wgs shell script and run shell
outfile=open("%s/fastq2vcf.sh"%(out_path),"w")
for(root, dirs, files) in os.walk(fastq_dir):
    for file in files:
        par = "dragen -f -r %s --enable-cnv true --enable-duplicate-marking true --output-format BAM --enable-map-align true  --enable-map-align-output true " \
              "--enable-bam-indexing true --enable-variant-caller true --enable-sv true " % (os.path.abspath(args.ref))
        array=file.split("_")
        name,file2,shell="","",""
        for i in range(0,len(array)-sample_name_suffix):
            name+=array[i]
            name+="_"
        name=name.strip("_")
        par += "--output-file-prefix %s --RGID %s_RGID --RGSM %s "%(name,name,name)
        ##################################################################################add PoN parameter
        if args.PoN != "false":
            par += " --cnv-normals-list %s --cnv-enable-self-normalization false --cnv-enable-gcbias-correction false " % (args.PoN)
        else:
            par += " --cnv-enable-self-normalization true --cnv-enable-gcbias-correction true "
        ##################################################################################
        if re.search(r'_R1_',file):
            file2=file.replace("_R1_","_R2_")
            par+=" -1 %s -2 %s "%(os.path.abspath(os.path.join(root,file)),os.path.abspath(os.path.join(root,file2)))
            if name in sample_wes:
                bed = os.path.abspath(args.bed)
                subprocess.check_call("mkdir -p %s/%s"%(wes_vcf,name),shell=True)
                par+="--vc-target-bed %s --sv-call-regions-bed %s --cnv-target-bed %s --sv-exome true --cnv-interval-width 1000 --output-directory %s/%s "%(bed,bed,bed,wes_vcf,name)
                outfile.write("%s\n"%(par))
            if name in sample_wgs:
                subprocess.check_call("mkdir -p %s/%s" % (wgs_vcf, name), shell=True)
                par+=" --output-directory %s/%s --repeat-genotype-enable=true --repeat-genotype-specs=/opt/edico/repeat-specs/hg19/ "%(wgs_vcf,name)
                outfile.write("%s\n" % (par))
outfile.close()
subprocess.check_call("sh %s/fastq2vcf.sh"%(out_path),shell=True)