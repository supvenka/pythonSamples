"""
Executing another py file here
file we are using is CmdLineArgsParseSample.py" where we provide mandatory and optional parameters
"""
import subprocess
import platform

command = "python"
fileName = "D:\SupDocs\Personal\Learnings\Python\Oracle_Python\CmdLineArgsParseSample.py"

osType = platform.system()

if osType == 'Windows':
    subprocess.call(['python',fileName, '-a PythonTraining.txt', '10' ,'cms'], shell = True)
else:
    pass

"""
Executing java program
"""
# subprocess.call(['javac', 'temp.java'])

