import os
import sys
import subprocess
import re

def run(samplesheet,bcldir,outdir):
    infile=open(samplesheet,"r")
    par=""
    for line in infile:
        line = line.strip()
        if re.search('Sample_ID', line) or re.search('Sample_Name', line):
            if re.search('Lane', line):
                par = " --no-lane-splitting false "
            else:
                par = " --no-lane-splitting true "
    infile.close()
    cmd="dragen -f --bcl-conversion-only true " \
         "--bcl-input-directory %s --output-directory %s " \
         "--sample-sheet %s %s "%(bcldir,outdir,samplesheet,par)
    if not os.path.exists("%s/Logs/FastqComplete.txt" % (outdir)):
        subprocess.check_call(cmd, shell=True)
        print("bcl2fastq finished\n")

if __name__=="__main__":
    if (len(sys.argv) != 4):
        print("\nusage:python3 %s samplesheet.csv bcl/ output/\n"
              "Email:yucai.fan@illumina.com\n"%(sys.argv[0]))
    else:
        run(sys.argv[1],sys.argv[2],sys.argv[3])