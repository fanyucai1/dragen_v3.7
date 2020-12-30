#1 gtf文件下载

https://hgdownload.soe.ucsc.edu/goldenPath/hg19/bigZips/genes/

https://hgdownload.soe.ucsc.edu/goldenPath/hg38/bigZips/genes/

#2  运行例子
    dragen --enable-rna=true --enable-single-cell-rna=true --umi-source=fastq  \
    -1 10X-PBMC-Rep1_S1_L001_R2_001.fastq.gz --umi-fastq=10X-PBMC-Rep1_S1_L001_R1_001.fastq.gz \
    -r /staging/reference/hg19_rna_v8/ -a /staging2/public/hg19_gtf/hg19.ensGene.gtf.gz \
    --single-cell-barcode-position=0_15 --single-cell-umi 16_27 --RGID=1 --RGSM=sample1 \
    --output-file-prefix=sample1 --output-dir=./

#3 10x 测序文库学习链接

    https://teichlab.github.io/scg_lib_structs/methods_html/10xChromium3.html

#4：