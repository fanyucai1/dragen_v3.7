#Email:yucai.fan@illumina.com
#2021.01.05 vserion:1.0
import os
import subprocess
import argparse
import re
import gzip
import sys

def run(indir,outdir):
    if not os.path.exists(outdir):
        subprocess.check_call('mkdir -p %s'%(outdir),shell=True)
    for(root, dirs, files) in os.walk(indir):
        for file in files:
            sample_name,file_result="","false"
            ###################################################################CNV
            if re.search('.cnv.vcf.gz$',file):
                sample_name = file.split(".cnv.vcf.gz")[0]
                file_in = gzip.open(os.path.join(root,file), 'rt')
                file_out =open(os.path.join(outdir, "%s.cnv.pass.vcf" % (sample_name)), "wt")
                for eachline in file_in:
                    if re.search('^#', eachline):
                        file_out.write(eachline)
                    else:
                        array = eachline.split("\t")
                        if array[6] == "PASS":
                            file_result = True
                            file_out.write(eachline)
                file_in.close()
                file_out.close()
                if file_result=="false":
                    subprocess.check_call('rm -rf %s'%(os.path.join(outdir, "%s.cnv.pass.vcf" % (sample_name))),shell=True)
                else:
                    subprocess.check_call('gzip -v %s'%(os.path.join(outdir, "%s.cnv.pass.vcf" % (sample_name))),shell=True)
                file_result = "false"
            ###################################################################SNP+Indel
            if re.search('.hard-filtered.vcf.gz$',file):
                sample_name = file.split(".hard-filtered.vcf.gz")[0]
                file_in = gzip.open(os.path.join(root,file), 'rt')
                file_out =open(os.path.join(outdir, "%s.hard-filtered.pass.vcf" % (sample_name)), "wt")
                for eachline in file_in:
                    if re.search('^#', eachline):
                        file_out.write(eachline)
                    else:
                        array = eachline.split("\t")
                        if array[6] == "PASS":
                            file_result = True
                            file_out.write(eachline)
                file_in.close()
                file_out.close()
                if file_result=="false":
                    subprocess.check_call('rm -rf %s'%(os.path.join(outdir, "%s.hard-filtered.pass.vcf" % (sample_name))),shell=True)
                else:
                    subprocess.check_call('gzip -v %s'%(os.path.join(outdir, "%s.hard-filtered.pass.vcf" % (sample_name))),shell=True)
                file_result = "false"
            ###################################################################SV
            if re.search('.sv.vcf.gz$',file):
                sample_name = file.split(".sv.vcf.gz")[0]
                file_in = gzip.open(os.path.join(root,file), 'rt')
                file_out =open(os.path.join(outdir, "%s.sv.pass.vcf" % (sample_name)), "wt")
                for eachline in file_in:
                    if re.search('^#',eachline):
                        file_out.write(eachline)
                    else:
                        array=eachline.split("\t")
                        if array[6] == "PASS":
                            file_result = True
                            file_out.write(eachline)
                file_in.close()
                file_out.close()
                if file_result=="false":
                    subprocess.check_call('rm -rf %s'%(os.path.join(outdir, "%s.sv.pass.vcf" % (sample_name))),shell=True)
                else:
                    subprocess.check_call('gzip -v %s'%(os.path.join(outdir, "%s.sv.pass.vcf" % (sample_name))),shell=True)
                file_result = "false"
            ###################################################################repeat
            if re.search('.repeats.vcf.gz$',file):
                sample_name = file.split(".repeats.vcf.gz")[0]
                file_in = gzip.open(os.path.join(root,file), 'rt')
                file_out =open(os.path.join(outdir, "%s.repeats.pass.vcf" % (sample_name)), "wt")
                for eachline in file_in:
                    if re.search('^#', eachline):
                        file_out.write(eachline)
                    else:
                        array = eachline.split("\t")
                        if array[6] == "PASS":
                            file_result = True
                            file_out.write(eachline)
                file_in.close()
                file_out.close()
                if file_result==True:
                    subprocess.check_call('gzip -v %s'%(os.path.join(outdir, "%s.repeats.pass.vcf" % (sample_name))),shell=True)
                else:
                    subprocess.check_call('rm -rf %s' % (os.path.join(outdir, "%s.repats.pass.vcf" % (sample_name))),
                                          shell=True)
                file_result = "false"
            ###################################################################
            if re.search('._coverage_metrics.csv$',file) or re.search('.fastqc_metrics.csv$',file) or re.search('mapping_metrics.csv$',file):
                subprocess.check_call('cp %s %s' % (os.path.join(root, file), outdir), shell=True)
    print("The process done.")

if __name__=="__main__":
    if len(sys.argv)==3:
        run(sys.argv[1],sys.argv[2])
    else:
        print("\nusage:python3 %s /dragen_result_dir/ /output_directoy/\n"%(sys.argv[0]))
        print("Email:yucai.fan@illumina.com")
