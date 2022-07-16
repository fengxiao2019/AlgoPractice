class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.in_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.in_stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(self.min_stack[-1], val))

    def pop(self) -> None:
        if not self.in_stack: return

        self.in_stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        if not self.in_stack: return None
        return self.in_stack[-1]

    def getMin(self) -> int:
        if not self.min_stack: return None
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()