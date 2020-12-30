import os
import subprocess

##download Kraken database:
###axel -n20 ftp://ftp.ccb.jhu.edu/pub/data/kraken2_dbs/old/minikraken2_v2_8GB_201904.tgz
outdir="/staging/fanyucai/dragen_meta"
prefix="test"
kraken_dir="/staging/reference/Kraken2/minikraken2_v2_8GB_201904_UPDATE/"
host_index="/staging/fanyucai/references/hg19"
pe1="/staging/fanyucai/dragen_meta/CoVOC43-95UHR-Illumina-cDNA-Synthesis-Unenriched-Rep2_S2_L001_R1_001.fastq.gz"
pe2="/staging/fanyucai/dragen_meta/CoVOC43-95UHR-Illumina-cDNA-Synthesis-Unenriched-Rep2_S2_L001_R2_001.fastq.gz"
cmd="dragen -f -r %s -1 %s -2 %s --metagenome-taxonomy %s/taxo.k2d --metagenome-options %s/opts.k2d --metagenome-index %s/hash.k2d " \
    "--output-directory %s --output-file-prefix %s --RGID RG --RGSM SM --Aligner.aln-min-score 50 --enable-sort false"\
    %(host_index,pe1,pe2,kraken_dir,kraken_dir,kraken_dir,outdir,prefix)
print(cmd)
#subprocess.check_call(cmd,shell=True)