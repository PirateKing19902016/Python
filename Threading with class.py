#https://pythonprogramming.net/threading-tutorial-python/

import threading
from queue import Queue
import time

class myThread(threading.Thread):
    def __init__(self, q):
        threading.Thread.__init__(self)
        self.q = q
    def run(self):
        while True:
            # gets an worker from the queue
            worker = self.q.get()

            # Run the example job with the avail worker in queue (thread)
            exampleJob(worker)

            # completed with the job
            self.q.task_done()

def exampleJob(worker):  # pretend to do some work.
    time.sleep(.5)
    with threading.Lock():
        print(threading.current_thread().name, worker)

# 20 tasks assigned.
q = Queue()
for worker in range(20):
    q.put(worker)


start = time.time()

# how many threads/worker are we going to allow for
for x in range(10):
    t = myThread(q)

    # classifying as a daemon, so they will die when the main dies
    t.daemon = True
    t.start()


q.join()
# wait until the thread terminates.

# with 10 workers and 20 tasks, with each task being .5 seconds, then the completed job
# is ~1 second using threading. Normally 20 tasks with .5 seconds each would take 10 seconds.
print('Entire job took:', time.time() - start)