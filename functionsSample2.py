# Required arguments : These are mandatory. The user must provide them when calling the function else error. Order of calling the argument should be followed as the func definition
# Keyword arguments : Here we provide the parameter name and the value, the order of the parameter can be anything
# Default arguments : Here if the user does not provide the value the default value specified in the definition is used. The default rgs should be in the end
# Variable length arguments: * is used to identify the rgument which is variable. It must be a tuple

# Required arguments
def displayInfo(name):
    print name

displayInfo("Suparna")

# Keyword arguments
def printInfo(name, age, gender):
    print "Name = ", name
    print "Age = ", age
    print "gender = ", gender

printInfo(age = 30, name = 'Oracle', gender ='F') # Order of calling does not match as we are providing it with parameterName and value
printInfo("Hello", gender='M', age=5) # here first we have given the value for name , other two we have used keyword which is fine, since in the def name is a string so order is followed

#Default arguments-optional arguments
#Rules - placed after the required arguments, can be multiple
def calculateEMI(amount, rate = 10, duration = 12):
    emi = amount * rate/100
    print "Amount =", amount
    print "Rate =", rate
    print "duration =", duration
    print "EMI = ", emi

calculateEMI(1000) #takes default value of rate = 10
calculateEMI(1000,20) #takes default value of rate = 20 user defined and default of duration as 12
calculateEMI(1000, duration=24)

#Rules- placed after required args, can have only one variable arg
# Cannot have default and variable paramters together
def joinStr(delimeter, *args):
    print " No of  arguments passed = ", len(args)
    print "Args = ", args
    return delimeter.join(args)

joinStr("-","a", "b", "c") # tuple passed contains 3 arguments
joinStr("*","oracle", "GE")

def add(*args):
    result = 0
    for i in args:
        result = result + i
        return result


print "10+20+30 = ", add(10,20,30)
print "20+30 = ", add(20,30)