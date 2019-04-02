data = "Hi! Good Morning! How are you?"

print"Data = ", data
print "Data length = ", len(data)
print "Data only alpha numberic = ", data.isalnum()
print "Data only digits = ", data.isdigit()
print "Data all chars in lower case = ", data.islower()
print "Data : Occurance of \!  = ", data.count("!")
print "Data : First Occurance of \!  = ", data.find('!')
print "Data : Last Occurance of \!  = ", data.rfind('!')

print "Find all occurrances in data ", data
startIndex = 0
noOfOccurs = data.count('!')
for i in range(noOfOccurs):
    index = data.find('!', startIndex)
    print "%d Occurrance at %d" % (i, index)
    startIndex = index + 1

splits = data.split()
print  "Splitted str = ", splits

print " --- Replace ----"
str1 =  data.replace('!', '*')
print "Replacing \! with * ", str1

print " --- Uppercase ----"
print "Uppercase of data =  ", data.upper()

print "first char: = " , data [0]
print "last char = ", data [-1]
print "chars between 5 and 10 = ", data [5:11] #Slicing
print "chars after index  5  = ", data [5:] #Slicing
print "First ten chars  = ", data [:11] #Slicing

print "All user ids should be 10 length"
userid = "admin"
print "UserId after left justified = ",userid.ljust(10, '-') # short of  width what to fill the empty with which char
print "UserId after right justified = ",userid.rjust(10, '-')
print "UserId after Center justified = ",userid.center(10, '-')
print "UserId after Zero fill = ",userid.zfill(10)





