"""
Output of one is the input to another using pipe
ex: ls -l | grep *.txt
output of ls -l will be given as input to grep
"""

import subprocess
import platform


# ls -al does not work on windows, so we need to understand which OS it is to currently run ls -al equivalent of that is dir is windows
osType = platform.system()
print "Current OS = ", osType

if osType == 'Darwin': #MAC
    pass
if osType == 'Windows':
    procHandle = subprocess.Popen(['dir'], stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE)
    # We now use the above procHandle 's output  as the INPUT to the below subprocess.PIPE
    # we use the stdin=procHandle.stdout  as stdin
    outProcHandle =subprocess.Popen(['findstr','.txt'], stdin=procHandle.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
    output = outProcHandle.communicate()[0] # [0] ---> implies only stdout Iam printing
    print " ==== ----output  ==== ---- "
    print  output
    print " ==== ---- stdErrData  ==== ---- "
    # ---> implies only std err Iam printing #Basicall [0],[1] are pipes we have provided in our Popen method like this stdout=subprocess.PIPE, stderr=subprocess.PIPE
    stdErrData = outProcHandle.communicate()[1]
    print stdErrData
    print "================"
else: #LINUS
    pass
