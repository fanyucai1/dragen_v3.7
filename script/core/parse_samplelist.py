import re
import sys

def run(samplelist):
    infile=open(samplelist,"r")
    par_name,num,sample_par=[],0,{}
    for line in infile:
        line=line.strip()
        num+=1
        array = re.split('[\s,]', line)
        if num==1:
            for i in range(1,len(array)):
                par_name.append(array[1])#默认第一行为参数名称
        else:
            if len(array)>1:
                for i in range(1, len(array)):
                    sample_par[array[0]]+="--"+par_name[i]+" "
                    sample_par[array[0]]+=array[i]+" "
            else:
                str[array[0]]="false"
    infile.close()
    return str

if __name__=="__main__":
    if len(sys.argv)!=2:
        print("usage:\npython3 %s sample.list\n"%(sys.argv[0]))
        print("\n#Email:yucai.fan@illumina.com\n")
    else:
        run(sys.argv[1])