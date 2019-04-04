import threading
import time

def squareMe(num):
    print "SquareMe executed by :" , threading.current_thread().name
    print "Square of {} = {}".format(num, num * num)
    time.sleep(2)

def cubeMe(num):
    print "cubeMe executed by :", threading.current_thread().name
    print "Cube of {} = {}".format(num, num**3)
    time.sleep(4)


t1 = threading.Thread(target=squareMe, args=(10,)) # single tuple should containing a trailing comma
t1.name = "T1_SquareMe_Thread"

t2 = threading.Thread(target=cubeMe, args=(10,)) # single tuple should containing a trailing comma
t2.name = "T2_cubeMe_Thread"

print "Threads are created..."
t1.start()
t2.start()
print "Both Threads are executing "

t1.join()
print "t1 is done .."

t2.join()
print "t2 is done.."