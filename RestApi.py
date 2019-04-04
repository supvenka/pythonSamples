# We can test using https://www.geonames.org/export/web-services.html which has a list of restapis that we can test
# http://api.geonames.org/postalCodeSearchJSON?postalcode=9011&maxRows=10&username=demo
# http://api.geonames.org/postalCodeSearchJSON?postalcode=9011&maxRows=10&username=shree --->using shree since this is our trainer's id
# JSON object is similar to a dictionary object {Key:value}

import requests
url = "http://api.geonames.org/postalCodeSearchJSON?postalcode=560043&maxRows=10&username=shree"
responseObj  = requests.get(url)
print "ResponseObj status code =" , responseObj.status_code
print "ResponseObj: Content from google =  : ", responseObj.content
print "----Response in Josn------"
print responseObj.json()
print "----------"
jsonArrayList = responseObj.json()['postalCodes']
for entry in jsonArrayList:
    print " place =" , entry['placeName']

print "----- Getting all Key value pair -----"
for entry in jsonArrayList:
    for key,val in entry.items():
        print "Key = {} : Value = {}".format(key, val)

    print "......................"

myDictObjJson = {
"adminCode2": "9999",
"adminCode1": "99999",
"adminName2": "99999",
"lng": 9.9999999,
"countryCode": "IN",
"postalCode": "L-9999",
"adminName1": "Supvenka",
"ISO3166-2": "DI",
"placeName": "SupvenkaPlace1",
"lat": 49.847514698584796
}
postObj  = requests.post(url,myDictObjJson)
print" Post response status code = ",postObj.status_code

# Not working for this url since there is No authentication
jsonPostArrayList = responseObj.json()['postalCodes']
for entry in jsonArrayList:
    if entry['placeName'] == 'SupvenkaPlace1':
        print "Post successfull"











