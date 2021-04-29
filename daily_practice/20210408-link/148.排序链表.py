"""
2021.04.08
148. 排序链表
可以借助合并排序的思想进行排序
eg：4->2->1->3->5
    4->2->1    3->5
    4->2  1    3 - 5
    4 2   1    5->3
    2->4  1
    1->2->4    5->3
    1->2->3->4->5

用到的思想：链表从中间节点切分， 有序链表的合并
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def split_link(head: ListNode) -> ListNode:
    # 边界条件处理
    if not head or head.next is None:
        return head, None

    slow = head
    fast = head
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    left = head
    right = slow.next
    slow.next = None
    return left, right


def merge_sorted_link(l1: ListNode, l2: ListNode):
    dummy = ListNode(-1)
    head = dummy
    while l1 and l2:
        if l1.val < l2.val:
            head.next = l1
            l1 = l1.next
        else:
            head.next = l2
            l2 = l2.next
        head = head.next
    left_l = l1 or l2
    head.next = left_l
    return dummy.next


def sort_list(head: ListNode) -> ListNode:
    # 边界条件处理
    if head is None or head.next is None:
        return head

    left, right = split_link(head)
    s_l = sort_list(left)
    s_r = sort_list(right)
    return merge_sorted_link(s_l, s_r)