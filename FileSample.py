"""
File Related operations
"""

def writeToFile(data):

     fp = open("PythonTraining.txt", "w") # default text mode else for imgs video then binary mode we then use "wb" # default mode is wt ie write text mode
     fp.write(data)
     fp.write("\n ---end of file----")
     fp.close()
     print "Data written...."

def readFromFile():
    fp = open("PythonTraining.txt") # default mode is rt ie read text mode
    data = fp.read(10) # returns a String
    print "First 10 chars = ", data
    print "File pointer position = ", fp.tell()
    data = fp.read() # all lines from the current file pointer location
    print "Remaining chars = ", data
    # read from the beginning
    fp.seek(0,0) # offset where - 0-beginning 1-current position 2-end of file

    print "File pointer position = ", fp.tell()
    data = fp.read()
    print " All data: ", data
    # when offset is negative that means we are traverse back words
    fp.seek(-10, 2)

    data = fp.read()
    print "Last 10 characters: ", data

    fp.close()

print __name__ # whne we run as an independant file it is run as a __main__
# If i donot put this condition when I import this class else where it will execute the below two calls . since it is considered as a  module to avoid we use the condition __main__ check
# so only when this class is executed it run the writeToFile and readFromFile
if __name__ == '__main__':
    writeToFile("Good Morning!, Python is a functional programming language")
    readFromFile()
