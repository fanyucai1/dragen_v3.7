import os
import subprocess
for i in "pyty":
    if i=="y":
        continue
    else:
        print(i)

r = subprocess.getoutput('which python3') +" " +"../core/bcl2fastq.py"
print(r)
subprocess.check_call(r,shell=True)