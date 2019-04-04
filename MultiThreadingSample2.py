import threading

counter = 0
def incrementCounter():
    global counter
    for _ in range(1000):
        print "incrementCounter :", threading.current_thread().name
        counter += 1


myCounter = 0
def incrementCounterWithLock(lockObj):
    global myCounter
    for _ in range(1000):
        print "incrementCounterWithLock :", threading.current_thread().name
        lockObj.acquire()
        myCounter += 1
        lockObj.release()



myLock = threading.Lock()

# Race condition -shared . two threads accessing the shared /same resource  we get race condition
# multiple threads accessing hte ahred resource. We should lock that resource . Then the thread should do the change and the next thread can then access it
# args not required since method incrementCounter does not have any parameter
# we are using (target=incrementCounter) without () like (target=incrementCounter())
# here we are not using  target=incrementCounter() ie no () because if we use () then it will call the method immediately .
# to avoid it to be called immediately we just give the method name. only when the thread start then the method will get called

t1 = threading.Thread(target=incrementCounter)
t1.name = "Thread_T1"
t2 = threading.Thread(target=incrementCounter) # args not required since method incrementCounter does not have any paramter
t2.name = "Thread_T2"

t1.start()
t2.start()
t1.join()
t2.join()

print " counter = ", counter
print ("\n")
print "---- Scenario2---Solve Race condn : using LOCK----"

t3 = threading.Thread(target=incrementCounterWithLock, args =(myLock,))
t3.name = "Thread_T3"
t4 = threading.Thread(target=incrementCounterWithLock, args =(myLock, ))
t4.name = "Thread_T4"

t3.start()
t4.start()
t3.join()
t4.join()

print " myCounter = ", myCounter
