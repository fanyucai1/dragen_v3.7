import re,sys,os,subprocess
sub=os.path.abspath(__file__)
dir_name=os.path.dirname(sub)
sys.path.append(dir_name)

def run(samplelist,config_file,indir):
    ################################
    infile=open(samplelist,"r")
    par_name,num,sample_par=[],0,{}
    for line in infile:
        num+=1
        array=line.strip().split(",")
        if len(array)>1:
            if num == 1:
                if len(array) > 1:
                    for i in range(0, len(array)):
                        par_name.append(array[i])  # 获得参数名
            else:
                sample_par[array[0]] = ""
                if len(array) > 1:
                    for i in range(1, len(array)):
                        sample_par[array[0]] += "--" + par_name[i] + " "
                        sample_par[array[0]] += array[i] + " "
                else:
                    sample_par[array[0]] = "false"
        else:
            exit()
    infile.close()
    for (root, dirs, files) in os.walk(indir):
        for sample_name in sample_par:
            tgex_script = "python3 %s/tgex_uploadSamples.py --config %s %s " % (dir_name, config_file,sample_par[sample_name])
            for file in files:
                if re.search(sample_name, file):
                    if re.search('.sv.pass.vcf.gz$', file):
                        tgex_script += " --svVcf %s " % (os.path.join(root, file))
                    if re.search('.hard-filtered.pass.vcf.gz$', file):
                        tgex_script += " --snvVcf %s " % (os.path.join(root, file))
                    if re.search('.cnv.pass.vcf.gz$', file):
                        tgex_script += " --cnvVcf %s " % (os.path.join(root, file))
            print(tgex_script)
            subprocess.check_call(tgex_script, shell=True)


if __name__=="__main__":
    if len(sys.argv)!=4:
        print("usage:\npython3 %s sample.list /path/to/tgex.config.yml /indir_vcf/\n"%(sys.argv[0]))
        print("\n#Email:yucai.fan@illumina.com\n")
    else:
        run(sys.argv[1],sys.argv[2],sys.argv[3])