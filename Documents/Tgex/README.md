# step1:

修改tgex.config.yml的相关信息

# step2:

    pip3 install PyYAML
    pip3 install requests

# step2:

上传对应的文件到tgex网站

    python3 tgex_uploadSamples.py --snvVcf sample.vcf.gz  --patientId *** --patientName sample1 --sampleRelation  Self --sampleTarget Exome --config tgex.config.yml --svVcf sample.sv.vcf.gz --cnvVcf sample.cnv.vcf.gz