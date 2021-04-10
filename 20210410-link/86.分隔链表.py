"""
86. 分割链表
https://leetcode-cn.com/problems/partition-list/
解题思路: 定义两个dummy 节点
bigger  -> 连接大于等于target的节点
smaller -> 连接小于target的节点
连接 smaller->bigger
时间复杂度：O(n)
空间复杂度：O(1)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def partition(head: ListNode, x: int) -> ListNode:
    dummy_big = ListNode(0)
    dummy_small = ListNode(-1)
    big = dummy_big
    small = dummy_small

    cur = head
    # 开始遍历处理每个节点
    while cur:
        if cur.val < x:
            small.next = cur
            small = small.next
        else:
            big.next = cur
            big = big.next

        cur = cur.next

    # 如果small 为空，直接返回big 节点
    if dummy_small.next is None:
        return dummy_big.next
    # 如果big 为空，直接返回small节点
    if dummy_big is None:
        return dummy_small.next

    # 拼接
    big.next = None
    small.next = dummy_big.next
    return dummy_small.next