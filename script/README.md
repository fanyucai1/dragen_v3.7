## bcl2vcf.py
**适用范围：从测序仪器下机的WGS与WES样本**

    python3 bcl2vc.py -r <ref> -i <bcl_directory> -s <SampleSheet.csv> -e wes.list -g wgs.list -o <output_directory>

  + 参数说明:<br>
      * -r 参考index**文件夹**<br>
      * -i 输入下机数据bcl**文件夹**<br>
      * -s 输入samplesheet<br>
      * -e 输入要分析的外显子样本名称，该文件为文本文件，一行为一个样本名称，样本名称需于samplesheet中保持一致<br>
          + -b 外显子bed文件与 **-e** 一起使用
      * -g 输入要分析的全基因组样本名称，该文件为文本文件，一行为一个样本名称，样本名称需于samplesheet中保持一致<br>
      * -o 输出目录<br>
      * -ne 外显子正常样本PoN list
      * -nw 全基因组正常样本PoN list
  + 示例:

    * wgs

          python3 bcl2vcf.py -i bcl/ -g wgs.list -s SampleSheet.csv -r /staging/reference/hg19_v8/ -o /output/ -ng normal_wgs.list
    * wes

          python3 bcl2vcf.py -i bcl/ -e exom.list -s SampleSheet.csv -b TruSeq_Exome_TargetedRegions_v1.2.bed -r /staging/reference/hg19_v8/ -o /output/ -ne normal_wes.list
  
    * wes+wgs

          python3 bcl2vcf.py -i bcl/ -g wgs.list -e exom.list -s SampleSheet.csv -b TruSeq_Exome_TargetedRegions_v1.2.bed -r /staging/reference/hg19_v8/ -o /output/ -ng normal_wgs.list -ne normal_wes.list