Table of Contents
=================

   * [Regions of homozygosity（ROH）](#regions-of-homozygosityroh)
   * [Force Genotyping](#force-genotyping)
   * [single cell](#single-cell)
   * [reference](#reference)



# Regions of homozygosity（ROH）

* 纯和缺失：一对同源染色体都发生了相同的缺失，含有这种同源染色体的生物称为缺失纯合子
* Gap >3M，在缺失区域没有SNV位点
* 不考虑性染色体
* 参数设置：--vc-enable-roh true

# Force Genotyping

* 条目解释

|Condition|Reported GT|
|:---|:---|
|At a position with no coverage|./.|
|At a position with coverage but no reads supporting ALT allele|0/0|
|At a position with coverage and reads supporting ALT allele|0/0 or 0/1 or 1/1 or 1/2|

# single cell

[hg19_gtf](https://hgdownload.soe.ucsc.edu/goldenPath/hg19/bigZips/genes/)<br>
[hg38_gtf](https://hgdownload.soe.ucsc.edu/goldenPath/hg38/bigZips/genes)<br>
[10x测序文库学习链接](https://teichlab.github.io/scg_lib_structs/methods_html/10xChromium3.html)

运行例子:

    dragen --enable-rna=true --enable-single-cell-rna=true --umi-source=fastq  \
    -1 10X-PBMC-Rep1_S1_L001_R2_001.fastq.gz --umi-fastq=10X-PBMC-Rep1_S1_L001_R1_001.fastq.gz \
    -r /staging/reference/hg19_rna_v8/ -a /staging2/public/hg19_gtf/hg19.ensGene.gtf.gz \
    --single-cell-barcode-position=0_15 --single-cell-umi 16_27 --RGID=1 --RGSM=sample1 \
    --output-file-prefix=sample1 --output-dir=./