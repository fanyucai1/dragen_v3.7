import subprocess
import os

outdir="/staging/fanyucai/dragen_RNA_Pathogen/analysis"
prefix="CoVOC43"
bed="RespiratoryVirus.20200409.bed"
ref_fa="NC_045512.2.fasta"
ref_dir="RespiratoryVirus_hg38_RNA"
script="/usr/bin/python3 /staging/soft/virus_coverage.py"
pe1="RNAEnrichment-10e1-viralcopies-RVOPv2-NextSeq_S6_L002_R1_001.fastq.gz"
pe2="RNAEnrichment-10e1-viralcopies-RVOPv2-NextSeq_S6_L002_R2_001.fastq.gz"

#DRAGEN Map/Align:
cmd="dragen --force --bin_memory 42949672960 --enable-map-align true --enable-rna true " \
    "--enable-duplicate-marking true --dupmark-version hash --enable-kmer true " \
    "--kmer-dropLowComplexity true " \
    "--kmer-kmerFASTA %s --kmer-reverseComplement true --output-format BAM " \
    "--qc-coverage-tag-1 pathogen --qc-coverage-region-1 %s " \
    "--qc-coverage-reports-1 overall_mean_cov hist contig_mean_cov cov_report full_res " \
    "--vc-target-bed %s --output-directory %s " \
    "--output-file-prefix %s " \
    "--enable-metrics-json true " \
    "--tumor-fastq1 %s --tumor-fastq2 %s " \
    "--ref-dir %s --RGSM-tumor %s --RGID-tumor %s"%(ref_fa,bed,bed,outdir,prefix,pe1,pe2,ref_dir,prefix,prefix)
#subprocess.check_call(cmd,shell=True)
if not os.path.exists("%s/vc"%(outdir)):
    os.mkdir("%s/vc"%(outdir))

#DRAGEN Variant Calling
cmd="dragen --bin_memory 42949672960 --output-directory %s/vc --output-file-prefix %s --enable-map-align false " \
    "--enable-variant-caller true --tumor-bam-input %s/%s_tumor.bam --enable-metrics-json true " \
    "--vc-ignore-cigar-skip-reads true --ploidy 1 --ref-dir %s" %(outdir,prefix,outdir,prefix,ref_dir)
#subprocess.check_call(cmd,shell=True)

out=outdir+"/"+prefix
#DRAGEN Variant Calling
cmd="%s %s %s.pathogen_cov_report.bed %s.pathogen_full_res.bed >%s.pathogen-coverage-report.tsv"\
    %(script,bed,out,out,out)
subprocess.check_call(cmd,shell=True)