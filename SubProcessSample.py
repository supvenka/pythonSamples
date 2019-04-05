import subprocess
import platform

# Passing the command as a list
responseCode = subprocess.call(['date', '/t'], shell=True)
print "responseCode = ", responseCode

# Passing as a string
responseCodeStr = subprocess.call('date /t', shell=True)
print "responseCodeStr = ", responseCodeStr

#Display output from the cmd prompt grap the o/p of the command within our programme

resultTodayDate = subprocess.check_output(['date', '/t'], shell=True) # This returns the o/p of the cmd passed and NOT the status
print "resultTodayDate = ", resultTodayDate

# There is an errorr in the command but this check_output does not give the exceptin or what went wrong if the cmd is incorrect
#resultTodayDateErr = subprocess.check_output(['incorrectCMd', '/t'], shell=True)
#print "resultTodayDate = ", resultTodayDate

# ls -al does not work on windows, so we need to understand which OS it is to currently run ls -al equivalent of that is dir is windows
osType = platform.system()
print "Current OS = ", osType

if osType == 'Darwin': #MAC
    lsOutput = subprocess.check_output(['ls -a'], shell=True)
    print "==== ---- LINUS ls -al  ----- ==="
    print lsOutput
if osType == 'Windows':
    outputDir = subprocess.check_output(['dir'], shell=True)
    print "==== ---- WINDOWS output Dir ----- ==="
    print outputDir
    print "==== ---- %%%%%%%%%%%%%%%%%%% ==="
    print "\n"
    print " ---- -- ----- ---Interactive Communicate with the process with PIPES ---- -- ----- ---"
    # output of Popen  command will be stored in the subprocess.PIPE
    # output is present in procHandle
    procHandle = subprocess.Popen(['dir'], stdout=subprocess.PIPE, shell=True)
    # We use the above subprocess.PIPE in our communicate , but we donot specifically mention it as an input to communicate.
    # we use the procHandle to communicate
    stdOutputData, stdErrData = procHandle.communicate() # gives 2 pipes one is stdout and stdErr
    print " $$$$$$ ==== ---- stdOutputData $$$$$$ ==== ---- "
    print  stdOutputData
    print " ++++++++ ==== ---- stdErrData  ==== ---- ++++++++"
    print stdErrData
    print "================"
else: #LINUS
    pass


# Collect the error exception in stdErr another pipe
procErrHandle = subprocess.Popen(['dirls'], stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE)
stdOutputErrData, stdErrDataOutput = procErrHandle.communicate()  # gives 2 pipes one is stdout and stdErr
print " $$$$$$ ==== ---- stdOutputErrData $$$$$$ ==== ---- "
print  stdOutputErrData
print " ++++++++ ==== ---- stdErrDataOutput  ==== ---- ++++++++"
print stdErrDataOutput
