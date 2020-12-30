#Tumor-normal

    dragen -f -r <HASHTABLE> \
    --output-directory <OUTPUT> --output-file-prefix <SAMPLE> \
    --enable-map-align false \
    --enable-cnv true \
    --tumor-bam-input <TUMOR_BAM> \
    --cnv-normal-b-allele-vcf <SNV_NORMAL_VCF> \
    --sample-sex <SEX>

* 输入tumor样本bam格式（必须）
* 输入normal样本VCF文件（必须）
* 可选参数--sample-sex FEMALE or MALE

#Tumor only

