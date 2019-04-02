adharDB = {}

#input from user
# His adhar number, Name of the person, mobile number and city
# save it in your dict

# Enter for three records
# Key adar num
# value is dictionary containing : key personName, key mobile value = number and Key city and value
# value {'name': , 'mobile':, 'city':}

for _ in range(3):
    name = raw_input("Enter Name :")
    mobile = raw_input("Enter mobile :")
    city = raw_input("Enter city :")
    while True:
        adharNum = raw_input("Enter adhar number :")
        if adharNum.isdigit() and len(adharNum) ==5:
            break
    adharDB[adharNum] = {'name': name, 'mobile':mobile, 'city':city}

print "******\n"
print adharDB

