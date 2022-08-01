import time
import threading
from emailer import Mail



class threadtester (threading.Thread):
    def __init__(self, id, name, i):
       threading.Thread.__init__(self)
       self.id = id
       self.name = name
       self.i = i
       
    def run(self):
       mail=Mail()
       mail.send('itmesreehari@gmail.com','hi','from multithreaded email') 
       thread_test(self.name, self.i, 5)
       print ("%s has finished execution " %self.name)

def thread_test(name, wait, i):

    while i:
       time.sleep(wait)
       print ("Running %s \n" %name)
       i = i - 1

if __name__=="__main__":
    thread1 = threadtester(1, "First Thread", 1)
    thread2 = threadtester(2, "Second Thread", 1)
    thread3 = threadtester(3, "Third Thread",2)

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()