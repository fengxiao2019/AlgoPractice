
import threading

"""
用Lock实现
"""
class Foo:
    def __init__(self):
        self.first_lock = threading.Lock()
        self.second_lock = threading.Lock()
        self.first_lock.acquire()
        self.second_lock.acquire()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_lock.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        with self.first_lock:
            printSecond()
        self.second_lock.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        with self.second_lock:
            printThird()

"""
用Condition实现
"""


class Foo:
    def __init__(self):
        self.exec_condition = threading.Condition()
        self.order = 0
        self.first_finished = lambda: self.order == 1
        self.second_finished = lambda: self.order == 2

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        with self.exec_condition:
            printFirst()
            self.order = 1
            self.exec_condition.notify(2)

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        with self.exec_condition:
            self.exec_condition.wait_for(self.first_finished)
            printSecond()
            self.order = 2
            self.exec_condition.notify()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        with self.exec_condition:
            self.exec_condition.wait_for(self.second_finished)
            printThird()

"""
用信号量实现
"""
class Foo:
    def __init__(self):
        self.semphores = [threading.Semaphore(0), threading.Semaphore(0)]

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.semphores[0].release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        with self.semphores[0]:
            printSecond()
            self.semphores[1].release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        with self.semphores[1]:
            printThird()

"""
用事件
"""
class Foo:
    def __init__(self):
        self.events = (threading.Event(), threading.Event())

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        # 通知在event[0]上等待的线程可以开始处理了
        self.events[0].set()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        self.events[0].wait()
        printSecond()
        # 通知在event[1]上等待的线程可以开始处理了
        self.events[1].set()


    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        self.events[1].wait()
        printThird()
        self.events[1].clear()