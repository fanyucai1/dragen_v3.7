dragen \
    -r ${1} \
    -1 ${2} -2 ${3} \
    --output-dir ${4} --output-file-prefix ${5} \
    --enable-map-align true \
    --enable-sort true --umi-enable true \
    --umi-correction-scheme=lookup \
    --RGID illumina --RGSM ${5} \
    --umi-min-supporting-reads 2