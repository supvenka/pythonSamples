"""
We should be able to open D:\SupDocs\Personal\Learnings\Python\Oracle_Python\PythonTraining.txt when I run this on cmd prompt
First to check if it woking on windows try it manually
open cmd promt and type the below:
start D:\SupDocs\Personal\Learnings\Python\Oracle_Python\PythonTraining.txt
"""

import subprocess
import platform
fileName = "D:\SupDocs\Personal\Learnings\Python\Oracle_Python\PythonTraining.txt"
osType = platform.system()

if osType == 'Windows':
    subprocess.call(['start',fileName], shell = True)
else:
    pass
