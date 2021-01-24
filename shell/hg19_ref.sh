####hg19(DNA+CNV+RNA)
dragen \
        --build-hash-table true \
        --ht-reference ${1} \
        --output-directory ${2} \
        --ht-alt-liftover /opt/edico/liftover/hg19_alt_liftover.sam \
        --ht-decoys /opt/edico/liftover/hs_decoys.fa \
        --enable-cnv true \
        --ht-num-thread 40 \
        --ht-build-rna-hashtable true