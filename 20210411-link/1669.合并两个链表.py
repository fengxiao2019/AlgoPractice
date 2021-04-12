# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        return merge_in_between(list1, a, b, list2)


    """
    1669. 合并两个链表
    1. 找到第a-1个节点
    2. 找到第b个节点
    3. 找到list2的尾部节点
    4. 链接list1的第a-1个节点到list2上
    5. 链接list2的tail节点到list2的第b+1个节点
    时间复杂度：O(n)
    空间复杂度：O(1)
    """


def merge_in_between(list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
    head = list1
    # 确定第a-1个节点， 只需要移动a-1次
    a_th_pre = head
    for i in range(1, b + 1):
        head = head.next
        if i == a - 1:
            a_th_pre = head
    a_th_pre.next = list2
    # 找到list2的尾部节点

    while list2 and list2.next:
        list2 = list2.next

    # 链接两个链表
    list2.next = head.next
    return list1