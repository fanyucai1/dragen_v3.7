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

# reference

血液病

[Short N J, Patel K P, Albitar M, et al. Targeted next-generation sequencing of circulating cell-free DNA vs bone marrow in patients with acute myeloid leukemia[J]. Blood Advances, 2020, 4(8): 1670-1677.](https://ashpublications.org/blood/article/132/Supplement%201/4212/275750/Targeted-Next-Generation-Sequencing-of-Cell-Free)

[Vicente A, Patel B A, Gutierrez-Rodrigues F, et al. Eltrombopag monotherapy can improve hematopoiesis in patients with low to intermediate risk-1 myelodysplastic syndrome[J]. Haematologica, 2020.](https://haematologica.org/article/view/9761)

性能验证

[Best practices for benchmarking germline small-variant calls in human genomes](https://www.nature.com/articles/s41587-019-0054-x)

[GA4GH Benchmarking Team GitHub repository](https://github.com/ga4gh/benchmarking-tools)

[hap.py benchmarking toolkit](https://github.com/Illumina/hap.py)

[Zhao S, Agafonov O, Azab A, et al. Accuracy and efficiency of germline variant calling pipelines for human genome data[J]. bioRxiv, 2020.](https://www.nature.com/articles/s41598-020-77218-4)

We can run [VCAT](https://www.illumina.com/products/by-type/informatics-products/basespace-sequence-hub/apps/variant-calling-assessment-tool.html) to produce recall and precision metrics for SNV and Indel.

科研方向(GWAS+小麦基因组）

[Yoo S K, Kim C U, Kim H L, et al. NARD: whole-genome reference panel of 1779 Northeast Asians improves imputation accuracy of rare and low-frequency variants[J]. Genome medicine, 2019, 11(1): 1-10.](https://genomemedicine.biomedcentral.com/articles/10.1186/s13073-019-0677-z)

[Zhao Y P, Fan G, Yin P P, et al. Resequencing 545 ginkgo genomes across the world reveals the evolutionary history of the living fossil[J]. Nature communications, 2019, 10(1): 1-10.](https://www.nature.com/articles/s41467-019-12133-5)

[Triticum aestivum Assembly and Gene Annotation](https://plants.ensembl.org/Triticum_aestivum/Info/Annotation/)

WGS+WES

[Wang H, Lu Y, Dong X, et al. Optimized trio genome sequencing (OTGS) as a first-tier genetic test in critically ill infants: practice in China[J]. Human Genetics, 2020, 139(4): 473-482.](https://link.springer.com/article/10.1007/s00439-019-02103-8)

[Clark M M, Hildreth A, Batalov S, et al. Diagnosis of genetic diseases in seriously ill children by rapid whole-genome sequencing and automated phenotyping and interpretation[J]. Science translational medicine, 2019, 11(489): eaat6177.](https://stm.sciencemag.org/content/11/489/eaat6177)

[Kingsmore S F, Cakici J A, Clark M M, et al. A randomized, controlled trial of the analytic and diagnostic performance of singleton and trio, rapid genome and exome sequencing in ill infants[J]. The American Journal of Human Genetics, 2019, 105(4): 719-733.](https://www.sciencedirect.com/science/article/pii/S0002929719303131)

[Jain A, Bhoyar R C, Pandhare K, et al. IndiGenomes: a comprehensive resource of genetic variants from over 1000 Indian genomes[J]. Nucleic Acids Research, 2020.](https://academic.oup.com/nar/advance-article/doi/10.1093/nar/gkaa923/5937082?login=true)

体细胞突变

[Deep whole-genome sequencing of 3 cancer cell lines on 2 sequencing platforms](https://www.nature.com/articles/s41598-019-55636-3#MOESM1)

[human HCC-1359 cell line](https://www.ebi.ac.uk/ols/ontologies/efo/terms?short_form=EFO_0002185)

[human HCC-1954 cell line](https://www.ebi.ac.uk/ols/ontologies/efo/terms?short_form=EFO_0001175)

SV性能验证

[Kosugi S, Momozawa Y, Liu X, et al. Comprehensive evaluation of structural variation detection algorithms for whole genome sequencing[J]. Genome biology, 2019, 20(1): 117.](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-019-1720-5)
