#命令行

        dragen -f -r ${1}  -a ${2}  -1 ${3} -2 ${4} \
        --RGID sample-RGID --RGSM sample-RGSM --output-file-prefix ${5} --output-dir ${6} \
        --enable-rna true --enable-rna-gene-fusion true --enable-rna-quantification true


#参数说明

* -r 参考基因组路径
* -a 基因组**gtf/gff**文件,下载链接：http://uswest.ensembl.org/info/website/upload/gff.html
   + [hg19](ftp://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_34/GRCh37_mapping/gencode.v34lift37.annotation.gtf.gz)
   + [hg38](ftp://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_34/gencode.v34.annotation.gtf.gz)

* -1 R1 fastq
* -2 R2 fastq
* --output-file-prefix 输出前缀
* --output-dir    输出结果路径

#分析输出结果

    <outputPrefix>.quant.sf 为转录本定量结果
    *.Chimeric.out.junction 基因融合输出结果
    SJ.out.tab 为可变剪切文件