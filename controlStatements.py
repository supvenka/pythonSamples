print "Control statements break, continue, pass"

print " ----- Break statement -----"
for ch in 'Oracle':
    if ch == 'a':
        break

    print "Letter : ", ch

print "Break statement Done"

print " ----- Continue statement -----"
for ch in 'Oracle':
    if ch == 'a':
        continue

    print "Letter : ", ch
print "Continue statement Done"

print " ----- Pass statement -----"
for ch in 'Oracle':
    if ch == 'a':
        # break
        # continue
        pass
    print "Letter : ", ch
print "Pass statement Done"


for i in range(3):
    print i
else:
    print "Loop is done"

