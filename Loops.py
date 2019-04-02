# For loop
"""Iterating over a sequence"""
print "---- For loop iterating over a sequence of characters ----"
for ch in "oracle":
    print "Alphabet = ", ch

print "---- For loop iterating over a list ----"
osList = [" Symbian", "Android", "iOs"]
for osName in osList:
    print "OS = ", osName

print "---- Square numbers from 0 to 5 ----"

for i in range(6):
    print "Square of ", i , " = ",i * i

print "---- Even number from 0 to 10 ----"

for i in range(0, 11,2):
    print "i =  ", i
    i = 1 # NOte here when we assign i = 1 i value changes when it starts from for it is the value in the list

print "---- Reverse or negative step size: Printing from 5 to 0 ----"
for i in range(5, -1,-1):
    print "i =  ", i


# While Loop : based on a condition
counter = 0
while counter < 3:
    print "counter = ", counter
    counter += 1 # There is no ++ operator in python

print " ----Nested Loop ----"
print " Tables of 21 to 25"

for number in range(21,26):
    print  " *** Table of " , number , " ****"
    for i in range(1,11):
        print number , " X " , i , " = ", number * i

