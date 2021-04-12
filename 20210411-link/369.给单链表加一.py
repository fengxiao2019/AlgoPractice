# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        return plus_one(head)


"""
369. 给单链表加一
解题思路: 翻转链表 + 1，然后再翻转回来
时间复杂度：O(n)，涉及到三次链表遍历
空间复杂度：O(1) 
"""


def reverse(head: ListNode, tail: ListNode):
    pre = None
    while head != tail:
        print(pre)
        tmp = head.next
        head.next = pre
        pre = head
        head = tmp
    return pre


def plus_one_1(head: ListNode) -> ListNode:
    if not head:
        return ListNode(1)
    r_head = reverse(head, None)

    carry = 1
    # 定义一个虚拟节点，帮助简化逻辑处理
    dummy = ListNode(0)
    new_head = dummy
    while r_head:
        sum_v = r_head.val + carry
        new_head.next = ListNode(sum_v % 10)
        carry = sum_v // 10
        new_head = new_head.next
        r_head = r_head.next
    if carry:
        new_head.next = ListNode(carry)
    return reverse(dummy.next, None)


"""
解题思路：递归解法
深度优先，每一层都返回上一层计算之后的carry
退出条件：head is None: return 1  
注意的地方：别忘记处理最后一个carry
"""


def plus_one(head: ListNode) -> int:
    if head is None:
        return ListNode(1)
    res = dfs(head)

    if res:
        new_head = ListNode(res)
        new_head.next = head
        return new_head
    return head


def dfs(head: ListNode) -> int:
    if head is None:
        return 1
    res = dfs(head.next)
    sum_v = head.val + res
    head.val = sum_v % 10
    return sum_v // 10
