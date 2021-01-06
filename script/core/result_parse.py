#Email:yucai.fan@illumina.com
#2020.11.09
#version 1.0
import os
import sys
import subprocess

def run(input_dir,prefix,output_dir):
    print(output_dir)
    if not os.path.exists(output_dir):
        subprocess.check_call("mkdir -p %s"%(output_dir),shell=True)
    outfile = open("%s/%s.tsv" % (output_dir, prefix), "w")
    outfile.write(
        "Sample name\tTotal reads\tTotal bases\tQ30(%)\tMapping(%)\tInsert length\tDuplication(%)\tCapture rate(%)\tMean coverage(X)\t20X coverage(%)\t50X coverage(%)\t100X coverage(%)\tUniformity of coverage (PCT > 0.2*mean)\n")
    for (root, dirs, files) in os.walk(input_dir):
        for file in files:
            if file.endswith("mapping_metrics.csv"):
                Sample_name = file.split(".")[0]
                file_coverage = os.path.join(root, "%s.target_bed_coverage_metrics.csv" % (Sample_name))
                if os.path.exists(file_coverage):
                    tmp = os.path.join(root, file)
                    infile = open(tmp, "r")
                    Total_reads, Dup_rate, Total_bases, Q30, mapping = "", "", "", "", ""
                    capture, coverage20x, coverage50x, coverage100x, mean_overage, Ploidy, Insert, Uniformity, target_reads = "", "", "", "", "", "", "", "", ""
                    for line in infile:
                        line = line.strip()
                        array = line.split(",")
                        if array[0] == "MAPPING/ALIGNING SUMMARY":
                            if array[2] == "Total input reads":
                                Total_reads = line.split(",")[-2]
                            if array[2] == "Number of duplicate marked reads":
                                Dup_rate = array[-1]
                            if array[2] == "Total bases":
                                Total_bases = array[-1]
                            if array[2] == "Q30 bases":
                                Q30 = array[-1]
                            if array[2] == "Properly paired reads":
                                mapping = array[-1]
                            if array[-2] == "Insert length: median":
                                Insert = array[-1]
                    outfile.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t" % (
                    Sample_name, format(int(Total_reads), ','), format(int(Total_bases), ','), Q30, mapping, Insert,
                    Dup_rate))
                    infile.close()
                    infile = open(file_coverage, "r")
                    for line in infile:
                        line = line.strip()
                        array = line.split(",")
                        if array[2] == "Aligned bases in target region":
                            capture = array[-1]
                        if array[2] == "PCT of target region with coverage [ 20x: inf)":
                            coverage20x = array[-1]
                        if array[2] == "PCT of target region with coverage [ 50x: inf)":
                            coverage50x = array[-1]
                        if array[2] == "PCT of target region with coverage [100x: inf)":
                            coverage100x = array[-1]
                        if array[2] == "Average alignment coverage over target region":
                            mean_overage = array[-1]
                        if array[2] == "Uniformity of coverage (PCT > 0.2*mean) over target region":
                            Uniformity = array[-1]
                    outfile.write("%s\t%s\t%s\t%s\t%s\t%s\n" % (
                    capture, mean_overage, coverage20x, coverage50x, coverage100x, Uniformity))
                    infile.close()
    outfile.close()
    
if __name__=="__main__":
    if len(sys.argv)!=4:
        print("usage:python3 %s input_dir/ prefix output_dir/\n")
        print("\nEmail:yucai.fan@illumina.com")
    else:
        run(sys.argv[1],sys.argv[2],sys.argv[3])