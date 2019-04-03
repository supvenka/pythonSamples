
"""
Oops concept: Class.
User defined class should be in Capital and inbuilt classes are lowercase ex str
In General the access specifiers are public by default
Common Data/Class variable are like static variable in Java. Accessed via class Name : In this example empCount , accessed via Employee.empCount
Dynamic Property: In python each obj  can have its own/extra variable/property or can remove a property of the class
__dict__ to get the all the attributes of the obj
To check for  attributes use hasattr(self,<attribute_name)
To make a attribute (Class variable or instance variable) private by prefix the attribute with double underscore __ ex __myaddr
To make instance variable private use __ for the attribute in the init method
We can also make methods by prefixing the methods with double underscore
Property decorator should be used for property/properties that is dependent on other instance variables (which are set in init function) ex: fullName is dependant on firstName and lastName
Property decorator  is used only on instance variables

Class decorator :operates on a class. Here we use decorator @classmethod and pass parameter cls
And access using cls.<propertyname>
And call it using class Name
"""

# Employee(object) ---> imlies Employee is inherited from object. This is good to have
class Employee(object):
    "Simple Employee class"

    # class variable : shared across allobjects : common data : like static in Java. If it modified by any instance the value is reflected across all objs
    empCount = 0

    # self is like this in Java ie obj ref
    # init is called when obj is created, like ctr
    # instance variables = firstName, lastName fullName, and salary
    def __init__(self, fName, lName, salary):
        self.firstName = fName
        self.lastName = lName
        self.__salary = salary

        # COmmenting the below to make it as a property decorator
        # self.fullName = fName + " " + lName

        # empCount is a class Variable . It is usually accessed using the ClassName
        Employee.empCount += 1
        print "Init is done"


    @property
    def fullName(self):
        return self.firstName + " " + self.lastName

    @classmethod
    def displayCount(cls):
        print "Employee Count = " , cls.empCount

    def displayInfo(self):
        print "Employee details: Full Name:", self.fullName # fullName is instance variable hence we refer it using self.
        print "Salary: ", self.__salary

    def applyBonus(self):
        if hasattr(self, 'bonus'): # checking if the obj has attribute bonus. Note it is called on self, since it is obj level
            self.__salary += self.bonus
        else:
            print " No Bonus attribute"
            # self.bonus = 10 or as below
            setattr(self, 'bonus', 10) # Setting the default value of bonus to 10

    def __myaddr(self):
        if hasattr(self, 'addr'):
            print "addr = ", addr


## end of class definition

# Creating objects of Employee class
emp1 = Employee("John","Smith", 1000)
emp2 = Employee("Merry","Rose", 2000)


print "Emp Count = ", Employee.empCount
emp1.displayInfo()

print "Full name of emp2 = " , emp2.fullName

#Dynamic property: Each obj can have its own property
emp1.bonus = 100 #add
print "Bonus of emp1: ", emp1.bonus
# print "Bonus of emp2: ", emp2.bonus This will give an error as emp2 does not have the bonus attribute
print "All the attributes of emp1 =", emp1.__dict__ # shows the newly added attr bonus as well

emp1.applyBonus()
# emp2.applyBonus() This will give an error as emp2 does not have the bonus attribute AttributeError: 'Employee' object has no attribute 'bonus'
# so we modified applyBonus method to add attr bonus using hasattr(self, 'bonus') if it does not then add attribute using setattr(self, 'bonus', 10)

emp1.lastName = "Laidlaw"
emp1.displayInfo() # here the last name for emp1 did NOT  change it remained Smith
# to solve the above we use the property decorator where we convert the method as an attribute. The method name shoud be the same name as the attribute

# To make your attribute private: we need to prefix the property with double underscore __ ex: __myaddr This is accessible only in the class
# here we made our salary as private using __salary

# To make a method private use __
# emp1.__myaddr() --> will give an error since this method is private and is called outside class

# Example for calling class decorator method using ClassName.method
Employee.displayCount()
emp1.displayCount() # we can still call it using instance
