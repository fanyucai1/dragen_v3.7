import sys
import subprocess
import os
import re

def run(ref, R1, R2, outdir, prefix,bed,list):
    if not os.path.exists(outdir):
        subprocess.check_call("mkdir -p %s"%outdir,shell=True)
    cmd="dragen -f -r %s -1 %s -2 %s "%(ref,R1,R2)
    cmd+=" --RGID Illumina_RGID --RGSM %s "%(prefix)
    cmd+=" --output-directory %s --output-file-prefix %s "%(outdir,prefix)
    cmd+=" --enable-duplicate-marking true --output-format BAM --enable-map-align true "
    cmd+=" --enable-map-align-output true --enable-bam-indexing true --enable-variant-caller true "
    cmd+=" --enable-cnv true --enable-sv true "
    cmd+=" --vc-target-bed %s --cnv-target-bed %s --sv-call-regions-bed %s "%(bed,bed,bed)
    cmd+=" --cnv-enable-self-normalization false  --sv-exome true --cnv-interval-width 500 "
    cmd+=" --cnv-normals-list %s "%(list)
    subprocess.check_call(cmd,shell=True)

def run2(ref,samplelist,fastq_dir,out_dir,normal,bed="false"):
    infile=open(samplelist,"r")
    samplename=[]
    for line in infile:
        samplename.append(line.strip().split(",")[0])
    infile.close()
    for (root,dirs,files) in os.walk(fastq_dir):
        for file in files:
            cmd = "dragen -f -r %s " % (ref)
            cmd += " --enable-duplicate-marking true --output-format BAM --enable-map-align true "
            cmd += " --enable-map-align-output true --enable-bam-indexing true --enable-variant-caller true "
            cmd += " --enable-cnv true --enable-sv true "
            if bed!="false":
                cmd += " --sv-exome true --vc-target-bed %s --cnv-target-bed %s --sv-call-regions-bed %s " % (bed, bed, bed)
            cmd += " --cnv-enable-self-normalization false --cnv-interval-width 500 "
            cmd += " --cnv-normals-list %s " % (normal)
            if re.search('fastq.gz$',file) and re.search("_R1_",file):
                R1=os.path.join(root,file)
                R2=R1.replace("_R1_","_R2_")
                for i in samplename:
                    cmd += " --RGID Illumina_RGID --RGSM %s " % (i)
                    cmd += " --output-directory %s/%s --output-file-prefix %s " % (out_dir, i,i)
                    if re.search(i,file):
                        cmd+=" -1 %s -2 %s "%(R1,R2)
                    subprocess.check_call(cmd,shell=True)

if __name__=="__main__":
    if len(sys.argv)<6:
        print("Usage:python3 %s ref/ /path/to/sample1.R1.fastq /path/to/sample1.R2.fastq /path/to/outdir/ /path/to/prefix /path/to/exon.bed /path/to/normal.list\n"%(sys.argv[0]))
        print("\npython3 %s /ref/ /path/to/samplelist /path/to/fastq-dir/ /path/to/outdir/ /path/to/PoN.list /path/to/exon.bed\n" %(sys.argv[0]))
        print("\npython3 %s /ref/ /path/to/samplelist /path/to/fastq-dir/ /path/to/outdir/ /path/to/PoN.list\n" % (sys.argv[0]))
        print("\nEmail:yucai.fan@illumina.com\n")
    if len(sys.argv) == 8:
        run(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7])
    if len(sys.argv) == 7:
        run2(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
    if len(sys.argv)==6:
        run2(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], bed="false")