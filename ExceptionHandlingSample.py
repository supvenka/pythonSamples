"""
Exception Handling
We must have a try followed by an except block or finally block
Valid
Try -except-else-finally
Try-else-finally
Try-except-else
Try -else only (not valid)
Try only
else is optional
"""

def writeToFile(data):
    try:
        #fp = open("FileDoesNotExist.txt")
        fp = open("PythonTraining.txt")
        fp.write(data)  # default is r mode .So it will throw an exception when we try to write to it IOError: File not open for writing
    except IOError as err: # catching the exception obj in err
        print "Either file opening has failed or Writing has failed..."
        print "Exception message: ", err.message
    except Exception as err:# Generic exception Handling since we do not know which error might occur:
        print "Unknown error: ", err.message
    else:# When there is no excepion  Good to have else so that we can confirm that the operation is successfully
        fp.close()
        print "Data written sucessfully"
    finally:
        print "Finally block This executes either exception occurred or not"

    print "Done..."


def writeAgain(data):
    try:
        fp = open("PythonTraining.txt")
    except IOError as err:
        print "IOError Opening failed", err.message
    else:
        try:
            fp.write(data)
        except IOError as err:
            print "Writing failed", err.message
        else:
            print "Data successfully written"
        finally:
            print " Inner Finally"
            fp.close()

writeToFile("Testing Exceptions...")
writeAgain("writingAgain")
