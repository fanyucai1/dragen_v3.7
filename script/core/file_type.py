import mimetypes
import re
import sys
import os

def run(infile,outdir):
    outdir=os.path.abspath(outdir)
    filetype=mimetypes.guess_type(infile)[0]
    outfile=""
    if not re.search('text/plain',filetype):
        infile=open(infile,"r",encoding='gbk')
        outfile=open("%s/unix_sample.list"%(outdir),"w",encoding='UTF-8')
        for line in infile:
            outfile.write(line)
        infile.close()
        outfile.close()
        return "%s/unix_sample.list"%(outdir)
    else:
        return infile

print(run(sys.argv[1],sys.argv[2]))