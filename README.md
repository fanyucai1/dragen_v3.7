Table of Contents
=================

   * [dragen](#dragen)
      * [Documents](Documents)
      * [quick start](#quick-start)
      * [input files](#input-files)
      * [output files](#output-files)
      * [FAQ](FAQ)
      * [reference](reference)

# dragen

## Documents

+   [用户使用手册](Documents/User-Guide.pdf)
+   [dragen-v3-7软件下载链接](https://sapac.support.illumina.com/downloads/illumina-dragen-v3-7-installers.html)
+   [MultiQC安装包](Documents/MultiQC-master.zip)
+   [dragen产品介绍.pdf](Documents/dragen产品介绍.pdf)
+   [开源压缩软件文档.pdf](Documents/开源压缩软件文档.pdf)
+   [dragen-压缩命令行说明.pdf](Documents/dragen-压缩命令行说明.pdf)
+   [dragen-TSO500-ctDNA数据分析文档.pdf](Documents/dragen-TSO500-ctDNA分析文档.pdf)
+   [dragen_v3.7更新说明文档.pdf](Documents/DRAGEN-v3.7更新说明文档.pdf)
+   [dragen服务器安装说明文档.pdf](Documents/dragen_v3服务器场地准备和安装指南.pdf)

## quick start

+   一键运行bcl2fastq数据拆分:[bcl2fastq.py](script/core/bcl2fastq.py)
+   一键运行fastq文件到vcf:[germline_fastq2vcf.py.py](script/core/germline_fastq2vcf.py)
+   一键运行统计dragen数据分析结果:[result_parse.py](script/core/result_parse.py)
+   一键建立CNV的PoN基线文件:[build_PoN.py](script/core/build_PoN.py)
+   一键提取dragen分析结果中的PASS位点:[copy2vcf.py](script/core/copy2vcf.py)
+   一键上传vcf到Tgex网站:[run_tgex.py](script/core/run_tgex.py)

## input files

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

## output files
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


## FAQ

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

## reference

* wgs/wes
  
1. [Wang H, Lu Y, Dong X, et al. Optimized trio genome sequencing (OTGS) as a first-tier genetic test in critically ill infants: practice in China[J]. Human Genetics, 2020, 139(4): 473-482.](https://link.springer.com/article/10.1007/s00439-019-02103-8)

2. [Clark M M, Hildreth A, Batalov S, et al. Diagnosis of genetic diseases in seriously ill children by rapid whole-genome sequencing and automated phenotyping and interpretation[J]. Science translational medicine, 2019, 11(489): eaat6177.](https://stm.sciencemag.org/content/11/489/eaat6177)

3. [Kingsmore S F, Cakici J A, Clark M M, et al. A randomized, controlled trial of the analytic and diagnostic performance of singleton and trio, rapid genome and exome sequencing in ill infants[J]. The American Journal of Human Genetics, 2019, 105(4): 719-733.](https://www.sciencedirect.com/science/article/pii/S0002929719303131)

4. [Jain A, Bhoyar R C, Pandhare K, et al. IndiGenomes: a comprehensive resource of genetic variants from over 1000 Indian genomes[J]. Nucleic Acids Research, 2020.](https://academic.oup.com/nar/advance-article/doi/10.1093/nar/gkaa923/5937082?login=true)

* 血液病

1. [Short N J, Patel K P, Albitar M, et al. Targeted next-generation sequencing of circulating cell-free DNA vs bone marrow in patients with acute myeloid leukemia[J]. Blood Advances, 2020, 4(8): 1670-1677.](https://ashpublications.org/blood/article/132/Supplement%201/4212/275750/Targeted-Next-Generation-Sequencing-of-Cell-Free)

2. [Vicente A, Patel B A, Gutierrez-Rodrigues F, et al. Eltrombopag monotherapy can improve hematopoiesis in patients with low to intermediate risk-1 myelodysplastic syndrome[J]. Haematologica, 2020.](https://haematologica.org/article/view/9761)

* 科研(GWAS)

1. [Yoo S K, Kim C U, Kim H L, et al. NARD: whole-genome reference panel of 1779 Northeast Asians improves imputation accuracy of rare and low-frequency variants[J]. Genome medicine, 2019, 11(1): 1-10.](https://genomemedicine.biomedcentral.com/articles/10.1186/s13073-019-0677-z)

2. [Zhao Y P, Fan G, Yin P P, et al. Resequencing 545 ginkgo genomes across the world reveals the evolutionary history of the living fossil[J]. Nature communications, 2019, 10(1): 1-10.](https://www.nature.com/articles/s41467-019-12133-5)

* 小麦研究

1. [Triticum aestivum Assembly and Gene Annotation](https://plants.ensembl.org/Triticum_aestivum/Info/Annotation/)

* somatic variants calling所用的数据集以及文献

1. [Deep whole-genome sequencing of 3 cancer cell lines on 2 sequencing platforms](https://www.nature.com/articles/s41598-019-55636-3#MOESM1)

2. [human HCC-1359 cell line](https://www.ebi.ac.uk/ols/ontologies/efo/terms?short_form=EFO_0002185)

3. [human HCC-1954 cell line](https://www.ebi.ac.uk/ols/ontologies/efo/terms?short_form=EFO_0001175)

* 评估变异检测性能参考文献以及工具

1. [Best practices for benchmarking germline small-variant calls in human genomes](https://www.nature.com/articles/s41587-019-0054-x)

2. [GA4GH Benchmarking Team GitHub repository](https://github.com/ga4gh/benchmarking-tools)

3. [hap.py benchmarking toolkit](https://github.com/Illumina/hap.py)

* 软件比较GATK, DRAGEN and DeepVariant

1. [Zhao S, Agafonov O, Azab A, et al. Accuracy and efficiency of germline variant calling pipelines for human genome data[J]. bioRxiv, 2020.](https://www.nature.com/articles/s41598-020-77218-4)

* 变异检测性能验证工具

1. We can run [VCAT](https://www.illumina.com/products/by-type/informatics-products/basespace-sequence-hub/apps/variant-calling-assessment-tool.html) to produce recall and precision metrics for SNV and Indel.


