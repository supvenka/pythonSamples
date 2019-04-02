print " ----- String format() -----"
personName = "John"
address = "Bangalore"
pincode = 560011

print " ----- Formatting using % - interpolation operator -----"
line = " %s resides at %s with pincode %d" % (personName, address, pincode)
print "Using % = ",line
print line
print "\n"

print " ----- Formatting using % - format method-----"
line = "{} resides at {} with pincode {}".format(personName, address, pincode)
print "Using str.format() = ",line

line = "{0} resides at {1} with pincode {1}. {0} is an Oracle employee".format(personName, address, pincode)
print "Using index based str.format() = ",line


print " ----- Formatting using % - interpolation operator 3 digit places ----"
for i in range(11):
    print "%03d" % i

print " ----- Formatting using % - interpolation operator 4 decimal places----"
latt = 12.89892344
longi = 77.343253
print "Lat = %.2f \nLongitude = %.4f" % (latt, longi)
