import sys
import subprocess
import os
import re

def run(ref,samplelist,fastq_dir,out_dir,bed,normal="false"):
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
            cmd += " --sv-exome true --vc-target-bed %s --cnv-target-bed %s --sv-call-regions-bed %s " % (bed, bed, bed)
            cmd += " --cnv-enable-self-normalization false --cnv-interval-width 500 "
            if normal!="false":
                cmd += " --cnv-normals-list %s " % (normal)
            if re.search('fastq.gz$',file) and re.search("_R1_",file):
                R1=os.path.join(root,file)
                R2=R1.replace("_R1_","_R2_")
                for i in samplename:
                    cmd += " --RGID Illumina_RGID --RGSM %s " % (i)
                    cmd += " --output-directory %s/%s --output-file-prefix %s " % (out_dir, i,i)
                    if re.search(i,file):
                        if not os.path.exists("%s/%s"% (out_dir,i)):
                            subprocess.check_call("mkdir -p %s/%s"% (out_dir,i),shell=True)
                        cmd+=" -1 %s -2 %s "%(R1,R2)
                    subprocess.check_call(cmd,shell=True)

if __name__=="__main__":
    if len(sys.argv)==6:
        run(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    elif len(sys.argv)==7:
        run(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
    else:
        print("\npython3 %s /ref/ /path/to/sample.list /path/to/fastq-dir/ /path/to/outdir/ /path/to/exon.bed /path/to/PoN.list\n" % (sys.argv[0]))
        print("\npython3 %s /ref/ /path/to/sample.list /path/to/fastq-dir/ /path/to/outdir/ /path/to/exon.bed\n" % (sys.argv[0]))
        print("\nEmail:yucai.fan@illumina.com\n")