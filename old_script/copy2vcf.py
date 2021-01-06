#Email:yucai.fan@illumina.com
#2021.01.05 vserion:1.0
import os
import subprocess
import argparse
import re
import gzip

parse=argparse.ArgumentParser("Copy files to new directory.\n")
parse.add_argument("-i","--indir",help="input directory",required=True)
parse.add_argument("-o","--outdir",help="output directory",required=True)
args=parse.parse_args()

if not os.path.exists(args.outdir):
    subprocess.check_call('mkdir -p %s'%(args.outdir),shell=True)
for(root, dirs, files) in os.walk(args.indir):
    for file in files:
        sample_name=""
        ###################################################################CNV
        if re.search('.cnv.vcf.gz$',file):
            sample_name = file.split(".cnv.vcf.gz")[0]
            file_result="false"
            file_in = gzip.open(os.path.join(root,file), 'rt')
            file_out =open(os.path.join(args.outdir, "%s.cnv.pass.vcf" % (sample_name)), "wt")
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
                subprocess.check_call('rm -rf %s'%(os.path.join(args.outdir, "%s.cnv.pass.vcf" % (sample_name))),shell=True)
            else:
                subprocess.check_call('gzip -v %s'%(os.path.join(args.outdir, "%s.cnv.pass.vcf" % (sample_name))),shell=True)
            file_result = "false"
        ###################################################################SNP+Indel
        if re.search('.hard-filtered.vcf.gz$',file):
            sample_name = file.split(".hard-filtered.vcf.gz")[0]
            file_result = "false"
            file_in = gzip.open(os.path.join(root,file), 'rt')
            file_out =open(os.path.join(args.outdir, "%s.hard-filtered.pass.vcf" % (sample_name)), "wt")
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
                subprocess.check_call('rm -rf %s'%(os.path.join(args.outdir, "%s.hard-filtered.pass.vcf" % (sample_name))),shell=True)
            else:
                subprocess.check_call('gzip -v %s'%(os.path.join(args.outdir, "%s.hard-filtered.pass.vcf" % (sample_name))),shell=True)
            file_result = "false"
        ###################################################################SV
        if re.search('.sv.vcf.gz$',file):
            sample_name = file.split(".sv.vcf.gz")[0]
            file_result = "false"
            file_in = gzip.open(os.path.join(root,file), 'rt')
            file_out =open(os.path.join(args.outdir, "%s.sv.pass.vcf" % (sample_name)), "wt")
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
                subprocess.check_call('rm -rf %s'%(os.path.join(args.outdir, "%s.sv.pass.vcf" % (sample_name))),shell=True)
            else:
                subprocess.check_call('gzip -v %s'%(os.path.join(args.outdir, "%s.sv.pass.vcf" % (sample_name))),shell=True)
            file_result = "false"
        ###################################################################repeat
        if re.search('.repeats.vcf.gz$',file):
            sample_name = file.split(".repeats.vcf.gz")[0]
            file_result = "false"
            file_in = gzip.open(os.path.join(root,file), 'rt')
            file_out =open(os.path.join(args.outdir, "%s.repeats.pass.vcf" % (sample_name)), "wt")
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
                subprocess.check_call('gzip -v %s'%(os.path.join(args.outdir, "%s.repeats.pass.vcf" % (sample_name))),shell=True)
            else:
                subprocess.check_call('rm -rf %s' % (os.path.join(args.outdir, "%s.repats.pass.vcf" % (sample_name))),
                                      shell=True)
            file_result = "false"
        ###################################################################
        if re.search('._coverage_metrics.csv$',file) or re.search('.fastqc_metrics.csv$',file) or re.search('mapping_metrics.csv$',file):
            subprocess.check_call('cp %s %s' % (os.path.join(root, file), args.outdir), shell=True)
print("The process done.")