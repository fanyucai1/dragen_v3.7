1.  拆分数据
python3 bcl2fastq.py /path/to/samplesheet.csv /path/to/bcl_directory/ /output_directory/

        *   /path/to/samplesheet.csv Samplesheet文件
        *   /path/to/bcl_directory/ 下机bcl文件夹
        *   /output_directory/  输出fastq文件夹

2.  运行从fastq到vcf
python3 germline_fastq2vcf.py -r /path/to/hg19_index/ -s /path/to/sample.list -b /path/to/exon.bed -p /path/to/PoN.list -f /path/to/fastq

        *   -r /path/to/hg19_index/ 参考基因组路径（required）
        *   -s /path/to/sample.list 分析样本sample.list（required）
        *   -b /path/to/exon.bed 分析样本对应的bed的文件
        *   -p /path/to/PoN.list    分析样本对应的PoN文件
        *   -f /path/to/fastq   分析样本对应的fastq文件夹（required）

3.  统计dragen的数据分析结果，并输出统计文件
python3 result_parse.py input_dir/ prefix output_dir/

        *   input_dir/  输入dragen数据分析结果目录
        *   output_dir/ 输出dragen数据分析统计结果文件夹

4.  批量构建PoN
python3 build_PoN.py /hg19_ref/ sample.list exon.bed fastq/ outdir/

        *   /hg19_ref/  参考基因组目录
        *   /sample.list/ 要分析样本sample.list
        *   /fastq/  输出fastq文件夹
        *   exon.bed    bed文件
        *   outdir/ 输出结果文件夹

5.  拷贝dragen所有样本的分析结果到一个文件夹，并提取所有PASS位点
    5-1. python3 core/copy2vcf.py /dragen_result_dir/ /output_directoy/
    
        *   /dragen_result_dir/ dragen数据分析结果文件夹
        *   /output_directoy/   输出结果文件夹
    
    基于5-1的输出上传tgex
    5-2.  python3 core/run_tgex.py sample.list /path/to/tgex.config.yml /indir_vcf/
    
        *   sample.list 样本sample.list
        *   /path/to/tgex.config.yml    Tge对应config文件
        *   /indir_vcf/ 输入vcf文件夹