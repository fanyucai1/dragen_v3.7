## bcl2vcf_dev.py

    usage: This script run from bcl to vcf.

     [-h] -i INDIR -s SAMPLESHEET -r REF [-e WES] [-b BED] [-g WGS] [-o OUTDIR] [-ne NORMAL_WES] [-ng NORMAL_WGS] [-c CONFIG]
    
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
      -ne NORMAL_WES, --normal_wes NORMAL_WES
                            exon normal list file
      -ng NORMAL_WGS, --normal_wgs NORMAL_WGS
                            wgs normal list file
      -c CONFIG, --config CONFIG
                            tgex config file


  * -r 参考index文件夹(required)
  * -i 输入下机数据bcl文件夹(required)
  * -s 输入samplesheet(required)
  * -e 外显子样本[sample.list](./test/sample.list)
  * -b 外显子bed文件与 **-e** 参数一起使用
  * -g 全基因组样本[sample.list](./test/sample.list)
  * -o 输出目录
  * -ne 外显子正常样本[PoN.list](./test/PoN.list)
  * -nw 全基因组正常样本[PoN.list](./test/PoN.list)
  * -c Tgex的config文件(tgex.config.yml)


备注：

**bcl2vcf_dev.py**需要设置python3路径<br>
**core/run_tgex.py**需要设置python3路径

##   FAQ:


1.  **bcl2vcf_dev.py**需要设置python3路径

2.  **core/run_tgex.py**需要设置python3路径