import threading
import time

def worker1():
    for i in range(1, 50):
        print("n                                                                                                                                                        " + str(i), end="\n")

def worker():
    for i in range(1, 50):
        print("t" + str(i), end="\n")
        if(i == 25):
            time.sleep(.5)



thread = threading.Thread(target=worker)
thread.start()
worker1()




