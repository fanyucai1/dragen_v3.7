bcl2vcf.py 脚本使用说明

    usage: This script run from bcl to vcf.
    
     [-h] -i INDIR -s SAMPLESHEET -r REF [-e WES] [-b BED] [-g WGS] [-o OUTDIR]
    
    optional arguments:
      -h, --help            show this help message and exit
      -i INDIR, --indir INDIR
                            bcl directory must be given(force)
      -s SAMPLESHEET, --samplesheet SAMPLESHEET
                            sample sheet must be given(force)
      -r REF, --ref REF     reference directory must be given(force)
      -e WES, --wes WES     exon sample list
      -b BED, --bed BED     bed file
      -g WGS, --wgs WGS     wgs sample list
      -o OUTDIR, --outdir OUTDIR
                            output directory
      -p PON, --PoN PON     PoN file

-i  输入下机数据bcl文件夹<br>
-s  输入样本Samplesheet<br>
-r  输入参考基因组文件夹<br>
-e  输入wes样本名称list，一行一样本名，必须与samplesheet中样本名一致<br>
-g  输入wgs样本名称list，一行一样本名，必须与samplesheet中样本名一致<br>
-b  bed文件<br>
-o  输出结果文件夹<br>
-p  PoN文件

