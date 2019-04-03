"""
Static Methods Operates ** neither **  on object or class variables
We use @staticmethod: These are used to manipulate outside the class variables.
Not used on instance or class variables
use property @staticmethod
These are mostly Utility classes that are used by other classes
Called using class Name
These do not have any class or instance variables defined in them
"""
class MathUtils(object):
    @staticmethod
    def add(a,b):
        return a+b

    @staticmethod
    def subtract(a,b):
        return a-b


# end of class

print MathUtils.add(10,20)
print MathUtils.subtract(20,10)