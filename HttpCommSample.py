"""
Http COnnection Sample
"""

import requests

# url = "http://google.com"
url = "http://sixty-north.com/c/t.txt"
responseObj  = requests.get(url)
print "ResponseObj status code =" , responseObj.status_code
print "ResponseObj: Content from google =  : ", responseObj.content





