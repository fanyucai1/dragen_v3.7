dragen -r ${1} -1 ${2} -2 ${3} \
              --RGSM ${4} --RGID illumina \
              --output-directory ${5} \
              --output-file-prefix ${4} \
              --enable-map-align true --enable-cnv true \
              --cnv-enable-gcbias-correction true \
              --cnv-enable-self-normalization false \
              --cnv-counts-method overlap --cnv-segmentation-mode cbs \
              --cnv-target-bed ${6} --cnv-interval-width 500
