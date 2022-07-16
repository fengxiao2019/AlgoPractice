"""
最小堆 Python 实现
"""


class MinHeap(object):
    def __init__(self):
        self.values = [None]

    def insert(self, value):
        self.values.append(value)
        index = len(self.values) - 1
        self.filter_up(index)

    def filter_up(self, index):
        """
        时间复杂度：O(log(n))
        """
        while index > 1: 
            pn = index // 2
            if self.values[pn] > self.values[index]:
                self.values[pn], self.values[index] = self.values[index], self.values[pn]
                index = pn
            else:
                break

    def check_valid(self):
        """
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        index = len(self.values) - 1
        while index > 1:
            pn = self.values[index // 2]
            # 父节点 必须小于子节点
            if pn > self.values[index]:
                break
            index -= 1
        return True

    def min_index(self, index, length):
        left = 2 * index
        right = left + 1
        min_value = self.values[index]
        min_index = index
        if left < length and self.values[left] < min_value:
            min_value = self.values[left]
            min_index = left
        if right < length and self.values[right] < min_value:
            # min_value = self.values[right]
            min_index = right
        return min_index

    def filter_down(self, index):
        length = len(self.values)
        while index < length:
            min_index = self.min_index(index, length)
            if min_index == index:
                break
            self.values[min_index], self.values[index] = self.values[index], self.values[min_index]
            index = min_index

    @property
    def length(self):
        return len(self.values)

    def remove(self, index):
        if index >= self.length or index <= 0:
            return
        # check the value of the node
        # if this is the root node or
        # the value of this node is the biggest value of its subnodes
        # filter down
        parent_node = index // 2
        self.values[index] = self.values[self.length - 1]
        self.values.pop(self.length - 1)
        if index == 1 or self.values[parent_node] < self.values[index]:
            self.filterDown(index)
        elif self.values[parent_node] > self.values[index]:
            self.filterUp(index)
