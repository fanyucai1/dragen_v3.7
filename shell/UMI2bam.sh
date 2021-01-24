mkdir -p ${1} && dragen -f \
    -r ${2} \
    -1 ${3} -2 ${4} \
    --output-dir ${1} --output-file-prefix ${5} \
    --enable-map-align true \
    --enable-sort true --umi-enable true \
    --umi-correction-scheme=lookup \
    --RGID Illumina_RGID --RGSM ${5} \
    --umi-min-supporting-reads 2