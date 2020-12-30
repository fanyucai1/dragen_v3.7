#Email:yucai.fan@illumina.com
#2020.11.16 version:1.0
#2020.11.30 version:2.0 fix bug:the samplesheet in '--no-lane-splitting'

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
parser.add_argument("-ne","--normal_exon",help="exon normal list file")
parser.add_argument("-nw","--normal_wgs",help="wgs normal list file")
args=parser.parse_args()
##########################################################check once again
tgex_script="/usr/bin/python3 /staging/Tgex/tgex_uploadSamples.py"
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
core.bcl2fastq.run(args.samplesheet,args.indir,args.outdir)
#########################################################get sample name

if args.wes:
    wes_vcf=out_path+"/wes_vcf"
    subprocess.check_call("mkdir -p %s"%(wes_vcf),shell=True)
    core.tgex_run(args.wes)

if args.wgs:
    wgs_vcf=out_path+"/wgs_vcf"
    subprocess.check_call("mkdir -p %s"%(wgs_vcf),shell=True)
    infile=open(args.wgs,"r")
    for line in infile:
        line = line.strip()
        array = line.split(",")
    infile.close()
###########################################################print wes or wgs shell script and run shell
outfile=open("%s/fastq2vcf.sh"%(out_path),"w")
outfile1=open("%s/vcf2tgex.sh"%(out_path),"w")
for(root, dirs, files) in os.walk(fastq_dir):
    for file in files:
        par = "dragen -f -r %s --enable-cnv true --enable-duplicate-marking true --output-format BAM --enable-map-align true  --enable-map-align-output true " \
              "--enable-bam-indexing true --enable-variant-caller true --enable-sv true " % (os.path.abspath(args.ref))
        array=file.split("_")
        name,file2,shell="","",""
        for i in range(0,len(array)-3):
            name+=array[i]
            name+="_"
        ###################从fastq文件识别样本名
        name=name.strip("_")
        par += "--output-file-prefix %s --RGID %s_RGID --RGSM %s "%(name,name,name)
        if re.search(r'_R1_',file):
            file2=file.replace("_R1_","_R2_")
            par+=" -1 %s -2 %s "%(os.path.abspath(os.path.join(root,file)),os.path.abspath(os.path.join(root,file2)))
            ###########################wes
            for i in range(0,len(sample_wes)):
                if sample_wes[i]==name:
                    bed = os.path.abspath(args.bed)
                    subprocess.check_call("mkdir -p %s/%s"%(wes_vcf,name),shell=True)
                    if args.normal_exon:
                        par += " --cnv-enable-self-normalization false --cnv-normals-list %s " % (args.normal_exon)
                    else:
                        par += " --cnv-enable-self-normalization true "
                    par+="--vc-target-bed %s --sv-call-regions-bed %s --cnv-target-bed %s --sv-exome true --output-directory %s/%s"%(bed,bed,bed,wes_vcf,name)
                    outfile.write("%s\n"%(par))
                    tegx_command=" %s --patientId %s --patientName %s --sampleRelation %s --sampleTarget "

            ###########################wgs
            if name in sample_wgs:
                subprocess.check_call("mkdir -p %s/%s" % (wgs_vcf, name), shell=True)
                par+=" --cnv-enable-self-normalization true --output-directory %s/%s --repeat-genotype-enable=true --repeat-genotype-specs=/opt/edico/repeat-specs/hg19/ "%(wgs_vcf,name)
                outfile.write("%s\n" % (par))
outfile.close()
outfile1.close()
subprocess.check_call("sh %s/fastq2vcf.sh"%(out_path),shell=True)