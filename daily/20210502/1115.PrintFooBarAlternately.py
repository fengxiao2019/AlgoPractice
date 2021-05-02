import threading


def PrintFoo():
    print('foo', end='')


def PrintBar():
    print('bar', end='')


class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_lock = threading.Lock()
        self.bar_lock = threading.Lock()
        self.bar_lock.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.foo_lock.acquire()
            printFoo()
            self.bar_lock.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.bar_lock.acquire()
            printBar()
            self.foo_lock.release()


class FooBar:
    def __init__(self, n):
        self.n = n
        self.barrier = threading.Barrier(2)

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            printFoo()
            self.barrier.wait()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.barrier.wait()
            printBar()


def main():
    foobar = FooBar(1)
    threadA = threading.Thread(target=foobar.foo, args=[PrintFoo])
    threadB = threading.Thread(target=foobar.bar, args=[PrintBar])
    threadA.start()
    threadB.start()
    threadA.join()
    threadB.join()


if __name__ == '__main__':
    main()

