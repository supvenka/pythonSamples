x = raw_input("Input number")
print "User entered value", x
try:
    x = float(x)
    inverse = 1/x
except ValueError as err:
    print "Please enter only numbers"
except ZeroDivisionError:
    print "Please enter only NON Zero number"
except: # This is equivalent to except Exception: If we want the error message use except Exception as err: print err.message
    print "Unknown error"
else:
    print "Inverse = ", inverse
finally:
    print "Done..."

