class Parent1(object):
    def displayInfo(self):
        print "Parent 1"


# end of Paren1 class

class Parent2(object):
    def displayInfo(self):
        print "Parent 2"

# end of Paren2 class

class Child(Parent1, Parent2):
    def displayInfo(self):
        super(Child, self).displayInfo()


# end of Child class

class Child2(Parent2, Parent1): # Different order of Parent
    def displayInfo(self):
        super(Child2, self).displayInfo()


# end of Child class


c = Child()
c.displayInfo()

print " -------------"
c2 = Child2()
c2.displayInfo()

