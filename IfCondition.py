number = raw_input("Enter any number:")
print type(number)
number = int(number)
print type(number)

if number > 0:
    print number, " is positive."
else:
    print number, "is negative."

if number % 2 == 0:
    print number, " is Even"
else:
    print number, " is Odd"

print "Else condition is NOT mandatory"

myNum = int(raw_input("Enter myNum value"))
print myNum
if myNum > 0:
    print myNum ," is positive"
elif myNum == 0: # Elif is executed only if the else condition is not met
    print myNum, " is Zero" # no else condition

print "In if condition it is not mandatory to have a elif or else condition"


# Nested if
marks = raw_input("Enter student marks")
print marks
if marks > 35:
    print "PASS"
    if marks > 75:
        print "DISTINCTION"
    elif marks > 65:
        print "FIRST CLASS"
    elif marks > 55: # This Elif is executed only if the else condition and the above elif  is not met. SO the order of elif matters
        print "SECOND CLASS"
    else:
        print "THIRD CLASS"
else:
    print "FAILED"



# logical Operators

if number > 0 and number % 2 == 0:
    print number, " is Even Positive number" # note here there is no else condition which is fine

# Simplyfying the baove

if number > 0 and not number % 2: # note here number % 2 == 0 gives ) as the result implies in if condn 0 means false hence NOT of false is true hence we use and not
    print number, " is Even Positive number"  # note here there is no else condition which is fine







