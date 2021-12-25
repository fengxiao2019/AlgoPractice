# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        return get_decimal2(head)


"""
递归调用
每一层返回上一次的和 以及 index 的值
边界条件：
if head is None:
    return 0, -1  # 0表示上一次的和， -1 表示退出的索引是-1
时间复杂度：O(n)
空间复杂度：O(n) 函数递归调用栈空间
"""


def helper(head: ListNode) -> (int, int):
    if head is None:
        return 0, -1
    sum_v, index = helper(head.next)
    if head.val:
        sum_v += pow(2, (index + 1))
    return sum_v, index + 1

def get_decimal_value(head: ListNode) -> int:
    if head is None: return 0
    sum_v, _ = helper(head)
    return sum_v

"""
1101 相当于最高位的1向右移了3位，次高位的1向右移了2位等
1101的演变方式可以看作：
1 >> 11 >> 110  >> 1101
可以用遍历模拟这种变化
时间复杂度：O(n)
空间复杂度：O(1)
"""
def get_decimal2(head: ListNode) -> int:

    sum_v = 0
    while head:
        sum_v = (sum_v << 1) + head.val
        head = head.next
    return sum_v