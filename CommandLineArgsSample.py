"""
Command Line Args:
Where we are executing a script to which the command line arguments are passed.
sys.args is a list that would retrieve the user provided inputs in the command line
"""

import sys
import os
print "No of arguments :", len(sys.argv)
print " Arguments passed = ", sys.argv

# Read file and display the content

if len(sys.argv) != 3:
    print " Please provide exactly One file name and the number of bytes to read..."
    exit()
else:
    fileName = sys.argv[1] # 0 is always the current executing script
    noOfBytesToRead = int(sys.argv[2]) # we need to convert to int else we get TypeError: an integer is required when we try to do fp.read(noOfBytesToRead)

if os.path.exists(fileName) and os.path.isfile(fileName):
    print " The provided value is a file and it exists"
    fp = open(fileName)
    data = fp.read(noOfBytesToRead)
    print "----- File contents------- "
    print data
    fp.close()
else:
    print "File does not exists. Or it is a directory"



