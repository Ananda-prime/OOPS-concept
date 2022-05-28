import threading



def display():
    for i in range(1,11):
        print("Display",i)

t = threading.Thread(traget = display)
t.start()

'''Synchronization method lock()'''
from threading import*
import time
l = Lock()
def  watchTV(name):
    l.acquire()
    print("Hi", end='')
    time.sleep(1)
    print(name, " is watching TV now")
    l.release

name1 = "Raja"
name2 = "Bala"
vivo = Thread(target = watchTV, agrs=(name1,))
dell = Thread(target = watchTV, agrs=(name2,))
vivo.start()
dell.start()

'''Synchronization method Rlock()'''
from threading import*
import time
def findFactorial(num):
    l.acquire()
    if num == 0:
        result = 1
    else:
        result = num * findFactorial(num-1)
    l.release()
    return result

def callFact(no):
    print("Result is ", findFactorial(no))

t1 = Thread(target=callFact, args=(4,))
t2 = Thread(target=callFact, args=(5,))
t1.start()
t2.start()