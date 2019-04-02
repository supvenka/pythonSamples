
print " --- More efficient when using not ----"

for number in range (2,21):
    print "Number = " , number
    # flag = False  remove this we donot need ths
    for divisor in range (2, number):
        if not number  % divisor :
            #flag = True
            break
    else:
        print "number is prime"

    # if not flag:
         #print number , " is prime"



print " --- While and else  ----"
counter = 0
while counter < 3:
    print "Counter = ", counter
    counter +=1
else: # This else executes when while condition is not met
    print"Counter is more than 3"
