# 常见问题

1. 多种类型的bed文件有什么区别

        _Covered.bed/*_Regions.bed - This BED file contains a single track of the genomic regions that are covered by one or more probes in the design. The fourth column of the file contains annotation information. You can use this file for assessing coverage metrics.
        _Padded.bed - This BED file contains a single track of the genomic regions that you can expect to sequence when using the design for target enrichment. To determine these regions, the program extends the regions in the Covered BED file by 100 bp on each side.

2. bed文件格式要求：必须有3列组成，另外列与列之间用tab隔开而不是空格

3. 第三方BAM输入Dragen报错，出现不兼容的情况

    + 可使用bedtools将bam文件转化为fastq再重新输入dragen:https://bedtools.readthedocs.io/en/latest/content/tools/bamtofastq.html
    
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

