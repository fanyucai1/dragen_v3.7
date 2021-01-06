import re
import sys

def run(samplelist):
    infile=open(samplelist,"r")
    tgex_par,num,str=[],0,{}
    for line in infile:
        line=line.strip()
        num+=1
        array = re.split('[\s,]', line)
        if num==1:
            for i in range(1,len(array)):
                tgex_par.append(array[1])
        else:
            if len(array)>1:
                for i in range(1, len(array)):
                    str[array[0]]+="--"+tgex_par[i]+" "
                    str[array[0]]+=array[i]+" "
            else:
                str[array[0]]=array[0]
    infile.close()
    return str

if __name__=="__main__":
    if len(sys.argv)!=2:
        print("usage:\npython3 %s sample.list\n"%(sys.argv[0]))
        print("\n#Email:yucai.fan@illumina.com\n")
    else:
        run(sys.argv[1])