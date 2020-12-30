## CNV

1. 解析度

   |WGS_Coverag_per_Sample|Recommended_Resolution*(bp)|
   |:---:|:---:|
   |5X   | 10000  |
   |10X   |  5000 |
   |>=30X   |  1000 |

**--cnv-interval-width** 用来控制解析度，WES默认是500，WGS默认是1000该参数在分析是需要设置，如果设置变小会增加分析时间

2. VCF结果解释

   |Diploid_or_Haploid|ALT|FORMAT CN|FORMAT_GT|
   |:---:|:---:|:---:|:---:|
   |Diploid|.|2|./.|
   |Diploid|DUP|>2|./1|
   |Diploid|DEL|1|0/1|
   |Diploid|DEL|0|1/1|
   |Haploid|.|1|0|
   |Haploid|DUP|>1|1|
   |Haploid|DEL|0|1|

3. Self Normalization算法不适合用于WES全外显子样本 **--cnv-enable-self-normalization true**

4. CNV默认分析参数: **--enable-cnv true --cnv-filter-copy-ratio 0.2 --cnv-filter-length 10000**

5. 概念
   + **CNV: copy number variation (deletions and duplications >50 bp).**<br>[Caspar S M, Dubacher N, Kopps A M, et al. Clinical sequencing: from raw data to diagnosis with lifetime value[J]. Clinical genetics, 2018, 93(3): 508-519.](https://onlinelibrary.wiley.com/doi/full/10.1111/cge.13190) <br>

   + **CNV refers to an intermediate scale structural variant, with copy number changes ranging from 1 Kb to 5 Mb of DNA**<br>
   [Kerkhof J, Schenkel L C, Reilly J, et al. Clinical validation of copy number variant detection from targeted next-generation sequencing panels[J]. The Journal of Molecular Diagnostics, 2017, 19(6): 905-920.](https://pubmed.ncbi.nlm.nih.gov/28818680/) <br>
   
   + **CNV size cutoffs were 1 kb for losses and 2kb for gains.**<br>[Lionel A C, Costain G, Monfared N, et al. Improved diagnostic yield compared with targeted gene sequencing panels suggests a role for whole-genome sequencing as a first-tier genetic test[J]. Genetics in Medicine, 2018, 20(4): 435-443.](https://www.nature.com/articles/gim2017119) <br>
   
   + **Constitutional deletions were defined by a mean ratio of 0.65 (1/2 alleles), and duplications were defined by a ratio of 1.35 (3/2 alleles)**

   + **Deletions were defined by a mean ratio of 0.8 (3/4 alleles), whereas duplications were defined by a ratio of 1.2 (5/4 alleles)**
   
   + **high copy number calls expected to have >0.85,and high copy number loss <-1.25**<br>[Chaubey A, Shenoy S, Mathur A, et al. Low Pass-Genome Sequencing: Validation and diagnostic utility from 409 clinical cases of low-pass genome sequencing for the detection of copy number variants (CNVs) to replace constitutional microarray[J]. The Journal of Molecular Diagnostics, 2020.](https://pubmed.ncbi.nlm.nih.gov/32344035/)
   
6. 对于靶向panel，关于CNV使用dragen以及建立PoN的处理可以参考以下文献<br> 
   [Patel B, Parets S, Akana M, et al. Comprehensive genetic testing for female and male infertility using next-generation sequencing[J]. Journal of assisted reproduction and genetics, 2018, 35(8): 1489-1496.](https://link.springer.com/article/10.1007/s10815-018-1204-7)