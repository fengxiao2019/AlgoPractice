"""
最小堆 Python 实现
"""

from typing import NoReturn, List


class MinHeap(object):
    """
    初始下标为1
    """
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

    def min_index(self, index: int, length: int) -> int:
        left = 2 * index
        right = left + 1
        # 记录当前节点的值
        min_value = self.values[index]
        min_index = index
        # 检查左节点是否存在，如果存在，检查左节点和当前值的关系
        if left < length and self.values[left] < min_value:
            min_value = self.values[left]
            min_index = left

        if right < length and self.values[right] < min_value:
            # min_value = self.values[right]
            min_index = right
        return min_index

    def filter_down(self, index: int) -> NoReturn:
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


"""
how to do in-place heap sort?
"""


def heapify(nums: List[int], index: int):
    """
    nums: 待排序的数组
    index: heap的长度
    """
    # index 为1 表示root节点
    # root 节点时，只有一个元素，默认满足堆的条件
    while index > 1:
        pn = index // 2
    # 检查 父子节点的关系
    # 如果想要构造最大堆，只需要调整一下 parent 节点和子节点的关系
        if nums[pn] > nums[index]:
            nums[pn], nums[index] = nums[index], nums[pn]
            index = pn
        else:
            break


def teardown(nums: List[int], length: int):
    index = 1
    while 2 * index < length:
        min_index = index
        if nums[index] > nums[2 * index]:
            min_index = 2 * index

        right = 2 * index + 1
        if right < length and nums[right] < nums[min_index]:
            min_index = right

        if min_index == index:
            break
        else:
            nums[min_index], nums[index] = nums[index], nums[min_index]
            index = min_index


def heap_sort(nums: List[int]):
    """
    nums: 待排序的数组
    返回正序排列
    """
    # 因为下标0我们不用，所以需要在开始位置插入一个0
    nums.insert(-1)
    for i in range(2, len(nums)):
        heapify(nums, i)

    # teardown
    for i in range(len(nums) - 1, 1, -1):
        tmp = nums[1]
        nums[1] = nums[i]
        teardown(nums, i)
        nums[i] = tmp
    return nums[1:][::-1]

