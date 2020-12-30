# PoN

## step1:
    
    sh PoN.sh /staging/human/reference/hg19_DNA_RNA_CNV/ /path/to/sample1.R1.fastq.gz /path/to/sample1.R2.gz sample1 /staging/human/PoN/test exon.bed

参数说明：

/staging/human/reference/hg19_DNA_RNA_CNV/ **参考基因组文件夹**<br>
/path/to/sample1.R1.fastq.gz **样本R1文件**<br>
/path/to/sample1.R2.fastq.gz **样本R2文件**<br>
sample1 **样本名称**<br>
/staging/human/PoN/test **输出结果路径**<br>
/path/to/exon.bed **外显子bed文件**<br>

## step2:

将 \<output-prefix\>.target.counts.gc-corrected.gz 文件写到normal.txt文本文件里,normal.txt内容如下：

    /data/output_trio1/sample1.target.counts.gc-corrected.gz
    /data/output_trio1/sample2.target.counts.gc-corrected.gz
    /data/output_trio2/sample4.target.counts.gc-corrected.gz
    /data/output_trio2/sample5.target.counts.gc-corrected.gz
    /data/output_trio3/sample7.target.counts.gc-corrected.gz
    /data/output_trio3/sample8.target.counts.gc-corrected.gz

## 附录说明

+ 建议基线样本数量50个左右

+ Segmentation参数<br>
        WES:          **--cnv-segmentation-mode cbs**<br>
        Germline WGS: **--cnv-segmentation-mode slm**<br>
        Somatic WGS:  **--cnv-segmentation-mode aslm**<br>

+ 如果你的靶向区域小于200,000，或者典型的靶向panel,建议不要进行GC Bias Correction<br>
        **--cnv-enable-gcbias-correction true**<br>
        **--cnv-enable-gcbias-smoothing true**<br>
        **--cnv-num-gc-bins 25**<br>

