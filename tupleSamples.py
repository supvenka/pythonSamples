"""
Tuples:
Immutable: cannot update
"""
data = 1,2,3 # donot provide (1,2,3)
print "data = ", data
#single element in a tuple

singleTuple = 1, # Need to have a , in the end
print "singleTuple = ", singleTuple

data = (1, 'John', 'Bangalore')

# data[0]= 2 Immutable: cannot update

#Iteration
for item in data:
    print "Item =", item

#Accessing
print "First tuple element = ", data[1]

mylist = list(data)
mylist.append(560043) # Adding to list
data = tuple(mylist) # converting list to tuple : Note this is not adding but a new reference of var data constructed using ctr
print "data = ", data
print "Id = ", id(data)