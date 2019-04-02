data = ['Java', 'C', 'C++', 'Java', 'Python']

#removal -del, remove(), pop()

print "Original data list = ", data
del data[1] # del is a statement
print "After deletion  data list = ", data

# remove an element
data.remove('Java') # Removes the first occurrance of the duplicate element
print "After Remove  data list = ", data


while 'Java' in data:
    data.remove('Java')

print data

# data.remove('Not present') # Not in list

data_duplicate = ['Java', 'C', 'C++', 'Java', 'Python']
javaOccr = data_duplicate.count('Java')
print "javaOccr = ", javaOccr
for _ in range(javaOccr):
    data_duplicate.remove('Java')

print "print data_duplicate = ",data_duplicate

if 'Ruby' in data:
    data.remove('Ruby')

data = ['Java', 'C', 'C++', 'Java', 'Python']
removedItem = data.pop()
print "Data = ",data
print "Data removed = ", removedItem

removedItem = data.pop(0)
print "Data = ",data
print "Removed = ", removedItem

#String to a list
mylist = list('Oracle Corporation')
print "mylist = ",mylist

#Reverse.
mylist.reverse()
print "mylist = ",mylist
# Converting the list to a str
print ''.join(mylist)

data = ['Java', 'C', 'C++', 'Java', 'Python']
#Slicing
print "Slicing data[1:3] = ",data[1:3]
print "First two elements data[:3] = ",data[:2]
print "last  two elements data[-2:] = ",data[-2:] # Left to right : beginning index should be less than the right index
print "Reverse = ",data[::-1] # : gives list from 0 index , now :-1 start
