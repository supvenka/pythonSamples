numberList = [1,2,3,4,5,6,7,10]

#List of even numbers

def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False

# The same evenList above  we can use a functional tool called filter shown in statement  print "Using filter ",filter(isEven, numberList)
evenList = []
for num in numberList:
    if isEven(num):
        evenList.append(num)


print evenList


# Rules  function that return boolean value
# Input argument : Single argument
# return value may be  the same length or a subset as that of the passed list

print "Using filter ",filter(isEven, numberList)
print "Using lambda", filter(lambda x: not x % 2, numberList)

# Square of numbers
numberList = [1,2,3,4,5,6,7,10]
def squareMe(n):
    return n * n

# Returning value , Single argument
# return value is of the same lenght as that of the passed list
squareList = map(squareMe, numberList) # We use tool map
print "Square of numbers = ", squareList

evenList = map(isEven, numberList) # We use tool map. Map gets the direct result of the function (isEven) here T or F  and puts in the map
print "evenList of numbers = ", evenList

# using lambda
squareList = map(lambda x:x*x, numberList)
print "using lambda = ", squareList

# Cmmulative sum
numberList = [1,2,3,4,5,6,7,10]
def add(a,b):
    return a + b

# Using reduce
# functions - exactly two arguments, return one value
cumulativeSum = reduce (add, numberList)
print "cumlative Sum = " , cumulativeSum
print "using lambda = ", reduce(lambda x,y: x+y, numberList)

numberList = [12,72,938,2372,568]

def max (a,b):
    if a > b :
        return a
    else:
        return b


maxNumber = reduce(max, numberList)
print  maxNumber
#C,Java -conditon?val1:val2
#In Python the above is used as ---> val1 if condition else val2
print "using lambda = ", reduce(lambda x,y: x if x > y else y, numberList)


numberList = [1,2,3,4,5,6,7,10]
#square of even numbers
# first get the even numbers
# then get the above results square

# This is list comprehension:  put it as a list
# Then the operation in th elist ie
# [ operation for ]
# or [ operation for <condition>] where conditio is optional
squareOfEven = [x * x for x in numberList if not x% 2]
print squareOfEven

#Cube of numbers
cube = [x ** 3 for x in numberList]
print cube

pinCodeList = ['560011', '123', '560068','234a']
#valid pincode : all digits and 6 length
validpincode =[ x for x in pinCodeList if x.isdigit() and len(x) ==6]
print validpincode

pinCodeList = ['560011', '123', '560068', '234'] # for element less than 6 fill it with 0
pincode = [x if len(x) == 6 else x.zfill(6) for x in pinCodeList]
print pincode

#valid names - only alphabets

myData = ['abc', 'xyz', 'a123', '09ab','pqr']
validmyData =[ x for x in myData if x.isalpha()]
print validmyData

#valid names - only alphabets else fill with ---
validmyDataHyphen =[ x if x.isalpha() else '---' for x in myData]
print validmyDataHyphen

