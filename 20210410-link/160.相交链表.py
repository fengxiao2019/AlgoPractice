"""
退出条件: start_a 和 start_b 相等就退出
相等：1. 相遇了 eg ：c1
     2. 不相遇 都为None
相遇：返回c1  不相遇返回none 所以退出循环直接返回start_a 就可以
时间复杂度：O(n)
空间复杂度：O(1)
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        start_a = headA
        start_b = headB

        while start_a != start_b:
            start_a = start_a.next if start_a else headB
            start_b = start_b.next if start_b else headA
        return start_a