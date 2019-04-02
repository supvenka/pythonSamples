# Prime numbers between 1 to 20 : 1 and the number itself is the divisor
for number in range (2,21):
    print "Number = " , number
    flag = False
    for divisor in range (2, number):
        if number % divisor == 0:
            flag = True

    if flag == False:
         print number , " is prime"



print " --- More effcient when using not ----"

for number in range (2,21):
    print "Number = " , number
    flag = False
    for divisor in range (2, number):
        if not number  % divisor :
            flag = True

    if not flag:
         print number , " is prime"


print " --- Using else with while and for ----"
print " --- Using else with while and for ----"






