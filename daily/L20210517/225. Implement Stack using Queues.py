from abc import ABC
from collections import deque
class MyStack(ABC):
    """
    实现方案：第一种，用两个队列
    in_queue 用来接收数据
    out_queue 用来弹出数据
    假设：out_queue = [4, 2, 9]
    现在来了一个7，现在，in_queue = [7], 我们想要的结果：[7, 4, 2, 9]
    我把out_queue的数据都接到in_queue，就可以得到[7, 4, 2, 9]，然后把这些数据全部转到out_queue
    这样，in_queue = [], out_queue = [7,4, 2, 9]

    实现方案2: 用一个队列
    假设当前queue = [4, 2, 9]
    来了一个新的元素：7，queue 变成 = [4, 2, 9, 7] 我们想要的结果是：[7, 4, 2, 9]
    我可以先把[4, 2, 9]逐个弹出来，再压入queue。
    queue 的变化过程：
    [4, 2, 9, 7]
    [2, 9, 7, 4]
    [9, 7, 4, 2]
    [7, 4, 2, 9] 得到结果
    """
    def __init__(self):
        raise NotImplementedError

    def push(self, x: int) -> None:
        raise NotImplementedError

    def pop(self) -> None:
        raise NotImplementedError

    def top(self) -> None:
        raise NotImplementedError

    def empty(self) -> None:
        raise NotImplementedError


class StackOfTwoDeque(MyStack):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.in_queue = deque()
        self.out_queue = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.in_queue.append(x)
        while self.out_queue:
            self.in_queue.append(self.out_queue.popleft())
        while self.in_queue:
            self.out_queue.append(self.in_queue.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.out_queue.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.empty(): return None
        return self.out_queue[0]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.out_queue) == 0


class StackOfOneDeque(MyStack):
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        length = len(self.queue)
        self.queue.append(x)
        for i in range(length):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0
