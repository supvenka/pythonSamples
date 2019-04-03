import os
import datetime

# os.mkdir("demoDir") # creates a directory in the current path. If dir already present gives an err

# os.rmdir("demoDir")
currentDir = os.getcwd()
print "Current working directory =", currentDir
os.mkdir("demoDir")

print "Change directory ", os.chdir(r""+currentDir) # raw r because we need to take care of the file seperators for O hence r as the user gives r 'C:\\myFolder\'

print "Listing current directory contents \n", os.listdir(os.getcwd())

fileName = "PythonTraining.txt"

print "Instead of using \\ or \/ we can use the join to join files"
fullPath = os.path.join(currentDir, fileName)

if os.path.exists(fullPath):
    if os.path.isfile(fullPath):
        print "--- File information ---"
        print "Size of file:" , os.path.getsize(fullPath)
        t = os.path.getmtime(fullPath)
        print " Last modified time = ", datetime.datetime.fromtimestamp(t)


def getDetails(dirpath):
    # list of subDircs, list of file
    # listdir-list
    # isFIle(), isDir()

    # 2 - list of files - recursively
    pass




