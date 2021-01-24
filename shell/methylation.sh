#methylation-protocol:none / directional / nondirectional / directional-complement
mkdir -p ${1} && dragen -f -r ${2} \
  -1 ${3} -2 ${4} --output-directory ${1} --output-file-prefix ${5} \
  --enable-methylation-calling true \
  --methylation-protocol ${6} \
  --RGID Illumina_RGID --RGSM ${5}