total = 0 # Global Scope
myTotal =0;
def sum(a,b):
    total = a + b
    print "Inside function , total = ", total

sum(10,20)
print "OutSide function , total = ", total

# now from inside the function I want to update the global variable total

def updateGlobal(a,b):
    global myTotal
    myTotal = a + b
    print "Inside function , total = ", myTotal

updateGlobal(10,30)
print "myTotal outside", myTotal

def sumAll(a,b):
    global total, counter
    total = a + b
    counter +=1
    print "Inside sumAll function , total = ", total


#print "counter outside", counter

#functiona taking function as argument

def doOperations(operation, a, b):
    operation(a,b)

doOperations(sum,1,2)

def subtract (a,b):
    print a-b

doOperations(subtract,10,5)





