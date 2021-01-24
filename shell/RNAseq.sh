####    RNA(Fusion+Quantification+splice junctions)
### hg19:ftp://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_34/GRCh37_mapping/gencode.v34lift37.annotation.gtf.gz
### hg38:ftp://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_34/gencode.v34.annotation.gtf.gz

mkdir -p ${1} && dragen -f -r ${2} -a ${3}  \
        -1 ${4} -2 ${5} \
        --RGID Illumina_RGID --RGSM ${6} \
        --output-dir ${1} --output-file-prefix ${6} \
        --enable-rna true --enable-rna-gene-fusion true --enable-rna-quantification true