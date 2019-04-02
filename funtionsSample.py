"""Functions Sample"""
def add(a,b):
    "Simple addition: a, b : both as int or str "

    if type(a) is int and type(b) is int:
       pass
    elif type(a) is str and type(b) is str:
        pass
    else:
        print "Invalid type"
        return

    result = a + b
    return result



c = add('hi', 'oracle') # strings are immutable : Pass by ref
print " c = ", c

d = add('hi', 3) # Invalid type

#Function overloading is not available in Python
def add(a,b,c):
    "Another add"
    return a+b+c

# print " 10 + 20 = " ,add(10,20) #TypeError: add() takes exactly 3 arguments (2 given
#Function overloading is NOT available in python
print "10+20+30 = " ,add(10,20,30)

print "To find the factorial of a number"
def factorial(n):
    "Calculates factorial of a number in a recursive way"
    if n == 1:
        return 1
    else:
        return n * factorial(n -1)

print "2! = ", factorial(2)
print "5! = ", factorial(5)



