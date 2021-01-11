1.  python3 bcl2fastq.py /path/to/samplesheet.csv /path/to/bcl_directory/ /output_directory/

*   /path/to/samplesheet.csv Samplesheet文件
*   /path/to/bcl_directory/ 下机bcl文件夹
*   /output_directory/  输出fastq文件夹

2.  python3 germline_fastq2vcf.py -r /path/to/hg19_index/ -s /path/to/sample.list -b /path/to/exon.bed -p /path/to/PoN.list -f /path/to/fastq

*   -r /path/to/hg19_index/ 参考基因组路径（required）
*   -s /path/to/sample.list 分析样本sample.list（required）
*   -b /path/to/exon.bed 分析样本对应的bed的文件
*   -p /path/to/PoN.list    分析样本对应的PoN文件
*   -f /path/to/fastq   分析样本对应的fastq文件夹（required）

3.  python3 result_parse.py input_dir/ prefix output_dir/
*   input_dir/  输入dragen数据分析结果目录
*   output_dir/ 输出dragen数据分析统计结果文件夹

4.  python3 build_PoN.py /hg19_ref/ sample.list exon.bed fastq/ outdir/
*   /hg19_ref/  参考基因组目录
*   sample.list 要分析样本sample.list
*   fastq/  输出fastq文件夹
*   