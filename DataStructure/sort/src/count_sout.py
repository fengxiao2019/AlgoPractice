import os
from time import sleep
import threading
from threading import Thread


def fun():
    print(f'获取线程id  {os.getpid()}')
    threading.stack_size(1)
    mydata = threading.local()
    mydata.vals = [{'i': i} for i in range(100)]
    print(mydata.__sizeof__())

thread = Thread(target=fun)
thread.start()
print(f'PID {os.getpid()}')
thread.join()