#Email:yucai.fan@illumina.com
#version:1.0
#2020.12.09-2020.12.11


import os
import sys
import subprocess
import argparse

parser=argparse.ArgumentParser("")
parser.add_argument("-n1","--n1",help="R1 normal fastq")
parser.add_argument("-n2","--n2",help="R2 normal fastq")
parser.add_argument("-t1","--t1",help="R1 tumor fastq")
parser.add_argument("-t2","--t2",help="R2 tumor fastq")
parser.add_argument("-p","--prefix",help="prefix of output",required=True)
parser.add_argument("-o","--outdir",help="output directory",default=os.getcwd())
parser.add_argument("-l","--library_type",help="umi-library-type",choices=["random-duplex—Dual","random-simplex—Single-ended","nonrandom-duplex—Dual"],required=True)
parser.add_argument("-t","--type",help="",choices=["FFPE","ctDNA"],required=True)
parser.add_argument("-r","--ref",help="rference hash index",required=True)
parser.add_argument("-b","--bed",help="bed file",required=True)
args=parser.parse_args()

if not os.path.exists(args.outdir):
    os.mkdir(args.outdir)
par="dragen -b %s -p %s -r %s -o %s " \
    "  --enable-map-align true --enable-sort true --umi-enable true --RGID %s-normal -–RGSM %s-normal "%(args.bed,args.prefix,args.ref,args.outdir,args.prefix,args.prefix)
if args.n1 and args.n2 and (not args.t1):
        par+=" -1 %s -2 %s "%(args.n1,args.n2)
if args.t1 and args.t2:
    par+= " --RGID-tumor %s-tumor -–RGSM-tumor %s-tumor "%(args.prefix,args.prefix)
    if args.type=="FFPE":
        par+=" --umi-min-supporting-reads=1 --vc-enable-umi-solid true --enable-variant-caller true "
    else:
        par+= " --umi-min-supporting-reads=2 --vc-enable-umi-liquid true --enable-variant-caller true "
    if args.n1 and args.n2:
        par+=" -1 %s -2 %s "%(args.n1,args.n2)
        par += " --RGID %s-normal -–RGSM %s-normal \ " % (args.prefix,args.prefix)
subprocess.check_call(par,shell=True)
