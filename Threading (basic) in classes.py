#https://www.pythoncentral.io/how-to-create-a-thread-in-python/

from threading import Thread
from random import randint
import time


class MyThread(Thread):

    def __init__(self, val):
        ''' Constructor. '''
        Thread.__init__(self)
        self.val = val

    def run(self):
        for i in range(1, self.val):
            print('Value %d in thread %s' % (i, self.getName()))

            # Sleep for random time between 1 ~ 3 second
            secondsToSleep =  randint(5,10)
            #print('%s sleeping fo %d seconds...' % (self.getName(), secondsToSleep))
            time.sleep(secondsToSleep)


# Run following code when the program starts
if __name__ == '__main__':
    start = time.time()
    # Declare objects of MyThread class
    myThreadOb1 = MyThread(4)
    myThreadOb2 = MyThread(4)
    myThreadOb3 = MyThread(4)
    myThreadOb4 = MyThread(4)

    myThreadOb1.setName('Thread 1')
    myThreadOb2.setName('Thread 2')
    myThreadOb3.setName('Thread 3')
    myThreadOb4.setName('Thread 4')

    # Start running the threads!
    myThreadOb1.start()
    myThreadOb2.start()
    myThreadOb3.start()
    myThreadOb4.start()

    # Wait for the threads to finish...
    myThreadOb1.join()
    myThreadOb2.join()
    myThreadOb3.join()
    myThreadOb4.join()

    print('Main Terminating...', time.time()-start)