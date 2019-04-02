add = lambda x,y:x+y
print add(20,30)

cube = lambda x: x ** 3
print cube(4)

joinStr = lambda *args: "-".join(args)
print joinStr("Hi", "Hello")

print "Passing a function name as a parameter in a function"
def doOperations(operation,a,b):
    print operation(a,b)

def subtract(a,b):
    print a-b

doOperations(subtract, 10,5)

print "Calling lambda as a function parameter"
doOperations(lambda x,y:x-y,40,20) # lambda , express and the parameters which have to be evaluated
