"""
When we have a class which is a Base class we need to specific object inheritance like this Employee(object)
"""
class Employee(object):
    " Base class for all employees"
    empCount = 0
    bonus = 100

    def __init__(self, fName, lname, salary):
        self.firstName = fName
        self.lastName = lname
        self.salary = salary

        Employee.empCount += 1
        print "Init of Employee done"

    def displayInfo(self):
        print "Name : ", self.firstName + " " + self.lastName
        print "Salary: " , self.salary

    def applyBonus(self):
        self.salary += Employee.bonus


## end of base Employee class

class Developer(Employee):
    bonus = 200
    def __init__(self, fName, lName, salary, skills):
        super(Developer, self).__init__(fName, lName, salary)
        self.skills = skills
        print "Init of Developer done"

    def displayInfo(self):
        print " --- Developer ---"
        super(Developer, self).displayInfo()
        print "Skills: ", self.skills

## end of base Developer class

class Tester(Employee):
    bonus = 150
    def __init__(self, fName, lName, salary, tools):
        super(Tester, self).__init__(fName, lName, salary)
        self.tools = tools
        print "Init of Tester done"

    def displayInfo(self):
        print " --- Tester ---"
        super(Tester, self).displayInfo()
        print "Testing tools : ", self.tools


## end of Tester class

emp1 = Employee("John", "Smith", 1000)
print " -------------"
emp2 = Developer("John", "Smith", 1000, "Python")
emp2.applyBonus()
emp1.displayInfo()

print " -------------"
emp3 = Employee("Merry", "Rose", 1000)
emp3.applyBonus()
emp3.displayInfo()

print " -------------"
emp4 = Tester("Mike", "Tyson", 1000, "Selenium")
emp4.applyBonus()
emp4.displayInfo()

listOfEmp = [emp1,emp2, emp3, emp4]
for emp in listOfEmp:
    emp.displayInfo() # Polymorphism method overriding at runtime based on which obj it holds it calls that class's displayInfo()
