Table of Contents
=================

   * [Documents](Documents/)
   * [Quick start](#quick-start)
   * [Input files](#input-files)
   * [Output files](#output-files)
   * [FAQ](#faq)
   * [Reference](#reference)
   * [Appendix](#Appendix)

# Quick start

+   一键运行bcl2fastq数据拆分:[bcl2fastq.py](script/core/bcl2fastq.py)
+   一键运行fastq文件到vcf:[germline_fastq2vcf.py.py](script/core/germline_fastq2vcf.py)
+   一键运行统计dragen数据分析结果:[result_parse.py](script/core/result_parse.py)
+   一键建立CNV的PoN基线文件:[build_PoN.py](script/core/build_PoN.py)
+   一键提取dragen分析结果中的PASS位点:[copy2vcf.py](script/core/copy2vcf.py)
+   一键上传vcf到Tgex网站:[run_tgex.py](script/core/run_tgex.py)

# Input files

* BAM
  + **germline:** -b sample.bam
  + **somatic:**  --tumor-bam-input tumor.bam
    
* fastq(.gz)
  + **WGS/WES**
    + -1 sample.R1.fastq -2 sample.R2.fastq
  + **Tumor only**
    + --tumor-fastq1 tumor.R1.fastq --tumor-fastq2 tumor.R2.fastq
  + **Tumor normal**
    + -1 sample.R1.fastq -2 sample.R2.fastq --tumor-fastq1 tumor.R1.fastq --tumor-fastq2 tumor.R2.fastq

# Output files
  + **SNV+Indel:**                \<output-file-prefix\>.hard-filtered.vcf.gz
  + **CNV:**                      \<output-file-prefix\>.cnv.vcf.gz
  + **repeat region:**            \<output-file-prefix\>.repeats.vcf.gz
  + **SV:**                       \<output-file-prefix\>.sv.vcf.gz
  + **ROH:**  \<output-file-prefix\>.roh.bed
    + Regions of homozygosity
    + 纯和子缺失：指一个个体的两条等位基因（alleles）都缺失了
    + 连续50个位点的纯和缺失，不包含杂合变异位点
    + 不考虑性染色体
    + 区域设置在3M
    + score: 
        + increases 0.025(homozygous variant) 
        + decreases with a large penalty (1–0.025) for every heterozygous SNV
  + **覆盖度统计文件:**      \<output-file-prefix\>.coverage_metrics.csv
  + **比对结果统计文件:**  \<output prefix\>.mapping_metrics.csv
  + **染色体倍型(适用全基因组):**      \<output prefix\>.ploidy.vcf.gz,\<output-file-prefix\>.ploidy_estimation_metrics.csv


# FAQ

1. 多种类型的bed文件有什么区别

        _Covered.bed/*_Regions.bed - This BED file contains a single track of the genomic regions that are covered by one or more probes in the design. The fourth column of the file contains annotation information. You can use this file for assessing coverage metrics.
        _Padded.bed - This BED file contains a single track of the genomic regions that you can expect to sequence when using the design for target enrichment. To determine these regions, the program extends the regions in the Covered BED file by 100 bp on each side.

2. bed文件格式要求：必须有3列组成，另外列与列之间用tab隔开而不是空格

3. 第三方BAM输入Dragen报错，出现不兼容的情况

    + 可使用[bedtools](https://bedtools.readthedocs.io/en/latest/content/tools/bamtofastq.html) 将bam文件转化为fastq再重新输入dragen
    
    + 首先可以尝试将BAM文件直接输入到Dragen进行重新比对生产BAM

          dragen -f -r /staging/human/reference/hg19_DNA_RNA_CNV/ \
          -b input.bam --enable-map-align true \
          --enable-map-align-output true \
          --enable-variant-caller true \
          --enable-sort true \
          --vc-sample-name Unsorted_SRA056922_30x_e10_50M \
          --output-directory /staging/examples/ \
          --output-file-prefix SRA056922_30x_e10_50M \
          --enable-duplicate-marking true

4. 挂载exFAT格式硬盘

        yum install -y http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm
        yum install exfat-utils fuse-exfat

5. 服务器清空缓存

        echo 3 > /proc/sys/vm/drop_caches

# Reference

* [wgs/wes](Documents/reference.md)
* [血液病](Documents/reference.md)
* [科研](Documents/reference.md)
* [somatic](Documents/reference.md)
* [评估变异检测性能参考文献以及工具](Documents/reference.md)

# Appendix

+   [dragen软件包](https://sapac.support.illumina.com/downloads/illumina-dragen-v3-7-installers.html)
+   [MultiQC安装包](Documents/MultiQC-master.zip)