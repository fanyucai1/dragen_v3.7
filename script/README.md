## bcl2vcf.py

    usage: This script run from bcl to vcf.

     [-h] -i INDIR -s SAMPLESHEET -r REF [-e WES] [-b BED] [-g WGS] [-o OUTDIR]
                                              [-ne NORMAL_WES] [-nw NORMAL_WGS]
    
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
      -nw NORMAL_WGS, --normal_wgs NORMAL_WGS
                            wgs normal list file

  * -r 参考index**文件夹**<br>
  * -i 输入下机数据bcl**文件夹**<br>
  * -s 输入samplesheet<br>
  * -e 外显子样本[samplelist](./template)样本名称需于samplesheet中保持一致<br>
      + -b 外显子bed文件与 **-e** 一起使用
  * -g 全基因组样本[samplelist](./template)样本名称需于samplesheet中保持一致<br>
  * -o 输出目录<br>
  * -ne 外显子正常样本PoN list
  * -nw 全基因组正常样本PoN list