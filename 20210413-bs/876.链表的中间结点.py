# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        return mid_node(head, None)

"""
给定一个头结点为 head 的非空单链表，返回链表的中间结点。

如果有两个中间结点，则返回第二个中间结点。


1     2     3  |    4    None     |
f           f  |           f      |
s     s     s  |                  |
从上图中可以看出
如果last_node 在3， s在2处返回   - 奇数个节点
如果last_node 在4， s在3处返回   - 偶数个节点
"""

def mid_node(head: ListNode, tail: ListNode) -> ListNode:
    if head == tail or head.next == tail:
        return head
    s,f = head, head
    while f != tail and f.next != tail:
        s = s.next
        f = f.next.next
    return s