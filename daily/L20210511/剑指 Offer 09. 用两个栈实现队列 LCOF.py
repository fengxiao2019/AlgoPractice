class CQueue:

    def __init__(self):
        self.enter = []
        self.out = []

    def appendTail(self, value: int) -> None:
        self.enter.append(value)


    def deleteHead(self) -> int:
        if not self.out:
            while self.enter:
                self.out.append(self.enter.pop())
        if not self.out: return -1
        return self.out.pop()




# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()