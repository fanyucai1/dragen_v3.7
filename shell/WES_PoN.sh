mkdir -p ${1} && dragen -f \
        -r ${2} \
        -1 ${3} -2 ${4} --output-file-prefix ${5} \
        --RGID Illumina_RGID --RGSM ${5} \
        --output-directory ${1} \
        --enable-duplicate-marking true \
        --output-format BAM --enable-sort true --enable-map-align true \
        --enable-map-align-output true \
        --enable-bam-indexing true \
        --enable-variant-caller true --vc-target-bed ${6} --cnv-enable-self-normalization false \
        --cnv-normals-list ${7} --cnv-enable-gcbias-correction false \
        --enable-cnv true --cnv-target-bed ${6} \
        --enable-sv true --sv-call-regions-bed ${6} --sv-exome true