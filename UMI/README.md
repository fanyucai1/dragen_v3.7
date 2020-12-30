# UMI 数据分析

## 数据拆分

UMI的样本的数据拆分与常规的拆分并不同，请参考文档进行数据拆分:

[UMI数据拆分.docx](UMI数据拆分.docx)

## UMI2bam

    sh UMI2bam.sh /path/to/reference sample1.R1.fastq(.gz)  sample1.R2.fastq(.gz) /path/to/outdirectory/ prefix
  + 参数说明
    + /path/to/reference 参考基因组目录
    + sample1.R1.fastq(.gz) 样本R1数据
    + sample1.R2.fastq(.gz) 样本R2数据
    + /path/to/outdirectory/ 结果输出文件夹
    + prefix 输出前缀


## call SNV

+ tumor-normal

        dragen -f -r <REF> --tumor-fastq1 <TUMOR_FASTQ1> \
        --tumor-fastq2 <TUMOR_FASTQ2> \
        --RGID-tumor RG0-tumor -–RGSM-tumor SM0-tumor \
        -1 <NORMAL_FASTQ1> \
        -2 <NORMAL_FASTQ2> \
        --RGID RG0-normal -–RGSM SM0-normal \
        --enable-variant-caller true \
        --output-directory <OUTPUT> --output-file-prefix <PREFIX> \
        --umi-enable true --vc-target-bed <target.bed>

+ tumor only

        dragen -f -r <REF> \
        --tumor-fastq1 <TUMOR_FASTQ1> \
        --tumor-fastq2 <TUMOR_FASTQ2> \
        --RGID-tumor RG0-tumor -–RGSM-tumor SM0-tumor \
        --enable-variant-caller true \
        --output-directory <OUTPUT> --output-file-prefix <PREFIX> \
        --umi-min-supporting-reads=1 --vc-enable-umi-solid true --umi-enable true --vc-target-bed <target.bed>

## 必设参数设置

--umi-library-type

+ **random-duplex—Dual** #双端随机UMI<br>
+ **random-simplex—Single-ended** #单端随机UMIs.<br>
+ **nonrandom-duplex—Dual** #非随机UMI，此时需同时指定**--umi-metrics-interval-file**<br>

--vc-enable-umi-liquid true --umi-min-supporting-reads=2 ##ctDNA样本~2000–2500X and target allele frequencies of 0.4% and higher

--vc-enable-umi-solid true  --umi-min-supporting-reads=1 ##FFPE样本~200—300X and target allele frequencies of 5% and higher