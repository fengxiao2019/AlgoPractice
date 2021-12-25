# 2.两数相加
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


"""
解题思路
   因为个位在头部，两个链表可以从head开始相加，但是要注意处理进位
   因为新链表的头部会不断后移，可以用一个哑巴节点记录下新链表的头部
   如果两个链表不能同时结束
   eg num1: 3->4->5->6->7
      num2: 3->4->5
    当num2 结束时，num1还没结束，需要继续处理num1，别忘了处理进位
    最后，如果进位不为0，别忘了处理进位
时间复杂度：O(m+n) m n 分别是l1 和 l2 链表的长度
空间复杂度：O(m+n) 新生成了最多m+n+1个节点
"""


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(-1)
    head = dummy
    carry = 0
    while l1 and l2:
        sum_val = l1.val + l2.val + carry
        val = sum_val % 10
        carry = sum_val // 10
        head.next = ListNode(val)
        head = head.next
        l1 = l1.next
        l2 = l2.next
    # 继续处理 未处理完的链表
    left_l = l1 or l2
    while left_l:
        sum_val = left_l.val + carry
        val = sum_val % 10
        # 别忘了上一个while 循环里面可能产生的进位
        carry = sum_val // 10
        head.next = ListNode(val)
        head = head.next
        left_l = left_l.next

    # 注意这里别忘记处理left_l可能产生的进位
    if carry:
        head.next = ListNode(carry)
    return dummy.next