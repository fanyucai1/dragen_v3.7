# hg38

1. download hg38 reference
   
   [hg38.fa](http://igenomes.illumina.com.s3-website-us-east-1.amazonaws.com/Homo_sapiens/UCSC/hg38/Homo_sapiens_UCSC_hg38.tar.gz)


2. 在v3.7最新版本中hg38支持Graph mapper,可以提高比对率(DNA+CNV+RNA)
   
       dragen --output-directory /staging/hash_table/human/hg38_CNV_RNA/ --build-hash-table true --ht-build-rna-hashtable true --enable-cnv true --ht-reference hg38.fa --ht-num-threads 40 --ht-alt-liftover /opt/edico/liftover/bwa-kit_hs38DH_liftover.sam --ht-pop-alt-contigs /opt/edico/liftover/pop_altContig.fa.gz --ht-pop-alt-liftover /opt/edico/liftover/pop_liftover.sam.gz --ht-pop-snps /opt/edico/liftover/pop_snps.vcf.gz

3. methylation

        dragen --output-directory /staging/hash_table/human/hg38_methylation/ --build-hash-table true --ht-reference hg38.fa --ht-alt-liftover /opt/edico/liftover/bwa-kit_hs38DH_liftover.sam --ht-decoys /opt/edico/liftover/hs_decoys.fa --ht-num-thread 40 --ht-methylated true

# hg19

1. DNA+CNV+RNA

        dragen --output-directory /staging/hash_table/human/hg19_CNV_RNA/ --build-hash-table true --ht-reference hg19.fa --ht-alt-liftover /opt/edico/liftover/hg19_alt_liftover.sam --ht-decoys /opt/edico/liftover/hs_decoys.fa --enable-cnv true --ht-num-thread 40 --ht-build-rna-hashtable true

2. methylation

        dragen --output-directory /staging/hash_table/human/hg19_methylation/ --build-hash-table true --ht-reference hg19.fa --ht-alt-liftover /opt/edico/liftover/hg19_alt_liftover.sam --ht-decoys /opt/edico/liftover/hs_decoys.fa --ht-num-thread 40 --ht-methylated true