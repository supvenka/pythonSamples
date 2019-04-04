# user defined exception class

class MyHTTPError(Exception):
    def __init__(self, message, errCode):
        self.message = message
        self.code = errCode

# end of MyHTTPError class

def doHTTPCommunication():
    # code for extasblishing the connection ie communicate to the remove server
    response = 500
    if response != 200:
        if response == 404:
            raise MyHTTPError ("File Not found", response)
        elif response == 500:
            raise MyHTTPError ("Server error", response)
        else:
            raise MyHTTPError ("Unknown Error", response)



# The user who uses the doHTTPCommunication method will write the below code

try:
    doHTTPCommunication()
except MyHTTPError as err:
    print "Message: = ", err.message
    print "Code: = ", err.code



