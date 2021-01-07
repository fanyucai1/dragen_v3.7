import sys
import subprocess
import os
import re
import argparse

parse=argparse.ArgumentParser("Run germline pipeline from fastq2vcf.")
parse.add_argument("-r","--ref",help="reference directory",required=True)
parse.add_argument("-s","--samplelist",help="sample list",required=True)
parse.add_argument("-o","--out_dir",help="output directory",required=True)
parse.add_argument("-b","--bed",help="bed file",default="false")
parse.add_argument("-p","--PoN",help="PoN list",default="false")
parse.add_argument("-f","--fastq_dir",help="fastq directory",required=True)
args=parse.parse_args()

infile=open(args.samplelist,"r")
samplename=[]
for line in infile:
    samplename.append(line.strip().split(",")[0])
infile.close()
for (root,dirs,files) in os.walk(args.fastq_dir):
    for file in files:
        cmd = "dragen -f -r %s " % (args.ref)
        cmd += " --enable-duplicate-marking true --output-format BAM --enable-map-align true "
        cmd += " --enable-map-align-output true --enable-bam-indexing true --enable-variant-caller true "
        cmd += " --enable-cnv true --enable-sv true "
        if args.PoN!="false":
            cmd += " --cnv-normals-list %s --cnv-enable-self-normalization false " % (args.PoN)
        else:
            cmd+=" --cnv-enable-self-normalization true "
        if args.bed !="false":
            cmd += " --sv-exome true --vc-target-bed %s --cnv-target-bed %s --sv-call-regions-bed %s --cnv-interval-width 500 " % (args.bed, args.bed, args.bed)
        else:
            cmd+=" --repeat-genotype-enable=true --repeat-genotype-specs=/opt/edico/repeat-specs/hg19/ "
        if re.search('fastq.gz$',file) and re.search("_R1_",file):
            R1=os.path.join(root,file)
            R2=R1.replace("_R1_","_R2_")
            cmd += " -1 %s -2 %s " % (R1, R2)
            for i in samplename:
                if re.search(i,file) and not os.path.exists("%s/%s/%s.time_metrics.csv"%(args.out_dir,i,i)):
                    cmd += " --RGID Illumina_RGID --RGSM %s " % (i)
                    cmd += " --output-directory %s/%s --output-file-prefix %s " % (args.out_dir, i, i)
                    if not os.path.exists("%s/%s"% (args.out_dir,i)):
                        subprocess.check_call("mkdir -p %s/%s"% (args.out_dir,i),shell=True)
                    subprocess.check_call(cmd,shell=True)