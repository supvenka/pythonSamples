"""
Raising an Exception : We can raise only inbuilt exception or user defined exception
"""
def add(a,b):
    if type(a) is int  and type(b) is int:
        pass
    elif type(a) is str  and type(b) is str:
        pass
    else:
        raise TypeError ("Either int and str")
    c = a + b
    print "Result = ", c

try:
    add(10, 20)
    add(10,"xyz") #InValid one string and one interger
except Exception as err:
    print err.message

