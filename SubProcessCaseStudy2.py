"""
Kill all chrome process
First check for the cmd if it works on windows
we can use cmd

cmd = "taskkill /F /IM chrome.exe"
"""

import subprocess
import platform

osType = platform.system()

if osType == 'Windows':
    subprocess.call(['taskkill', '/F','/IM','chrome.exe'], shell = True)
else:
    pass


