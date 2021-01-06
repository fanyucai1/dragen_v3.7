import sys
import subprocess
import os


def run(ref, R1, R2, outdir, prefix,bed):
    if not os.path.exists(outdir):
        subprocess.check_call("mkdir -p %s"%outdir,shell=True)
    cmd="dragen -f -r %s -1 %s -2 %s "%(ref,R1,R2)
    cmd+=" --RGID Illumina_RGID --RGSM %s "%(prefix)
    cmd+=" --output-directory %s --output-file-prefix %s "%(outdir,prefix)
    cmd+=" --enable-duplicate-marking true --output-format BAM --enable-map-align true "
    cmd+=" --enable-map-align-output true --enable-bam-indexing true --enable-variant-caller true "
    cmd+=" --enable-cnv true --enable-sv true "
    cmd+=" --vc-target-bed %s --cnv-target-bed %s --sv-call-regions-bed %s "%(bed,bed,bed)
    cmd+=" --cnv-enable-self-normalization true  --sv-exome true --cnv-interval-width 500 "
    subprocess.check_call(cmd,shell=True)

if __name__=="__main__":
    if len(sys.argv)!=7:
        print("Usage:python3 %s ref/ sample1.R1.fastq sample1.R2.fastq outdir/ prefix exon.bed\n"%(sys.argv[0]))
        print("\nEmail:yucai.fan@illumina.com\n")
    else:
        run(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])