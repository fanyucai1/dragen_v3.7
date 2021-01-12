import os
import subprocess
import sys
import re

def run(ref,samplelist,bed,indir,outdir):
    outdir=os.path.abspath(outdir)
    if not os.path.exists ("%s/test"%outdir):
        subprocess.check_call("mkdir -p %s/test"%(outdir),shell=True)
    sample_name=[]
    infile=open(samplelist,"r")
    outfile=open("%s/normal.list"%(outdir),"w")
    for line in infile:
        sample_name.append(line.strip().split(",")[0])
    for (root,dirs,files) in os.walk(indir):
        for file in files:
           if re.search('fastq.gz$',file) and  re.search('_R1_',file):
                R1=os.path.join(root,file)
                R2=R1.replace("_R1_","_R2_")
                for i in sample_name:
                    if re.search(i,file):
                        PoN_script = "dragen -r %s -1 %s -2 %s --RGSM %s --cnv-target-bed %s --output-directory %s/test --output-file-prefix %s " \
                                     "--RGID illumina --enable-map-align true --enable-cnv true " \
                                     "--cnv-enable-self-normalization false " \
                                     "--cnv-interval-width 1000" %(ref,R1,R2,i,bed,outdir,i)
                        subprocess.check_call(PoN_script,shell=True)
                        outfile.write("%s/%s.target.counts.gz\n" % (outdir,i))
    outfile.close()
    subprocess.check_call("cp %s/test/*target.counts.gz %s && rm -rf %s/test"%(outdir,outdir,outdir),shell=True)
if __name__=="__main__":
    if len(sys.argv)!=6:
        print("usage:python3 %s /hg19_ref/ sample.list exon.bed fastq/ outdir/\n"%(sys.argv[0]))
        print("\nEmail:yucai.fan@illumina.com\n\n")
    else:
        run(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])