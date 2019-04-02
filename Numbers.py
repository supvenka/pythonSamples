"""
My Numbers example
"""
x = 10
y = 3.0
z = 20
a = 3
z=20

print "x/y = ", x/y
print "x//y = ", x//y # Floored value ie converting the result to  an int
print "x//a = ", x//a

print "x % y = ", x % y
divOp = divmod(x,y)
print "Divmod of (x,y) = ", divOp
print type(divOp)
print "Division: ", divOp[0] # accessing the first part
print "23 to power of 12 = ", pow(23, 12) # pow is a part of in-built python library
print "Second way : 23 to power of 12 = ", 23 ** 12

z += 10 # Z= Z+ 10
print "Z = ", z

import math
print "Sqrt of 127 = ", math.sqrt(127) # sqrt is a part of math module hence we need to import math and not pow (which is in-built)