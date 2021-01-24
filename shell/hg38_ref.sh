####hg38
dragen --ht-reference ${1}\
--output-directory ${2} \
--build-hash-table true --ht-build-rna-hashtable true \
--enable-cnv true --ht-num-threads 40 \
--ht-alt-liftover /opt/edico/liftover/bwa-kit_hs38DH_liftover.sam \
--ht-pop-alt-contigs /opt/edico/liftover/pop_altContig.fa.gz \
--ht-pop-alt-liftover /opt/edico/liftover/pop_liftover.sam.gz \
--ht-pop-snps /opt/edico/liftover/pop_snps.vcf.gz