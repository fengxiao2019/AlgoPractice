"""
剑指 Offer 22. 链表中倒数第k个节点
解题思路： 快慢指针
思想：希望快指针结束时，慢指针刚好在倒数第k个节点上
1. 定位 slow 为head, slow = head, f = head
2. 确定 fast 指针: for i in range(k): f = f.next , 但是要注意处理边界条件
3. 同时前进快慢指针，步长都为1，当快指针结束时，慢指针就倒数第k个
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def get_kth_from_end(head: ListNode, k: int) -> ListNode:
    slow, fast = head, head
    for i in range(k):
        if not fast:
            return None
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    return slow
