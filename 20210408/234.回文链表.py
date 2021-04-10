"""
234. 回文链表
# 思路
步骤1: 从中间断开，变成两个链表 l 和 r
步骤2: 翻转链表r
步骤3: 检查r和l是否一致，退出条件是r 结束

边界条件处理：
1. 链表为空  返回False
2. 链表长度为1 返回 True

当链表的长度为偶数时，l的长度 == r的长度
当链表的长度为奇数时，l的长度 == r的长度 + 1
"""


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


# 分割链表
def split_link(head):
    if not head or head.next is None:
        return head, None

    slow, fast = head, head
    # 必须要这种，才能使得L1的长度 >= L2
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    left = head
    right = slow.next
    slow.next = None
    return left, right


# 翻转链表
def reverse_link(head):
    if not head or head.next is None:
        return head
    pre = None
    while head:
        tmp = head.next
        head.next = pre
        pre = head
        head = tmp
    return pre


# 检查链表是否相等

def check_same(l1: ListNode, l2: ListNode) -> bool:
    while l2 and l1:
        if l1.val == l2.val:
            l1 = l1.next
            l2 = l2.next
        else:
            return False
    return True


def is_palindrome(head: ListNode) -> bool:
    l, r = split_link(head)  # 切分链表
    r = reverse_link(r)  # 翻转右链表
    return check_same(l, r)  # 检查链表