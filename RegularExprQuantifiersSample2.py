import re
str1 = "john 1234 12/12/2000 , merry 893 01-02-1994 2333 1/1/98"

#DOB
print "Get on DOB =",re.findall(r'\d+[/-]\d{1,2}[/-]\d{2,4}',str1)

#only year of birth

print "Get on Year Of birth =",re.findall(r'\d+[/-]\d{1,2}[/-](\d{2,4})',str1)

str2 = "12.23.10.1 127.0.0.1 23.34 100.1.11"
print "Valid Ip =",re.findall(r'\b\d+\.\d+\.\d+\.\d+',str2)

str3 = "test@oracle1.com, abc@test.com, xyz@gmail.com"
print "Only domain names " ,re.findall(r'@(\w+\.\w+)',str3)

logs = """ Err log #1
debug log #10 msg
error log #100 err"""
#log id
print "Only log id ",re.findall(r'#(\d+)',logs)

str4 = "ant bat orange umbrella mango"
print "Words starting with vowels: ",re.findall(r'\b[aeiou]\w+',str4)
print "Words NOT starting with vowels: ",re.sub(r'\b[aeiou]\w+','',str4) # '' is used to replace


