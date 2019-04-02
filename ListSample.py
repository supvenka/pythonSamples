"""Lists Example
Append, extend, insert, remove del """
data = ['c', 'c++', 'Java', 100, 200]

#Operations
print "Number of elements in my list = ", len(data)
print "First element: ", data[0]
print "Last element: ", data[-1]

#Member ship
print "Is python in mylist = ", 'python' in data
print "Is Java in mylist = ", 'Java' in data

if 'Python' in data:
    print "Available in the list"
else:
    print "Not present in the list"

print "-- Enumerate through a list ---"
for indx, item in enumerate(data):
    print "Index = {}, Value = {}".format(indx, item)

print "-- Iterations through a list ---"
for item in data:
    print "Item = ", item

print "-- Index of an element ---"
print "Index of C++ = ", data.index('c++')


print "-- Adding elements to the list = etxend, append, insert"
data.extend(['Python', 'Ruby'])
print " Extending the list data = ", data

data.append('Java')
print " Appending to the list data = ", data
print " Adding a tuple to the list data "
data.append(('R', 'Go'))
# data =  ['c', 'c++', 'Java', 100, 200, 'Python', 'Ruby', 'Java', ('R', 'Go')]
print " data = ", data # See the output the whole tuple is added as one element to the list

print " data = ", data
data.insert(0, 'Java')
print " data = ", data

print " Updating at a specific index "
print " data[0] = ", data[0]
data[0] = 'javaScript'
print " After updating  data [0] = ", data[0]














