# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        return remove_nth_from_end(head, n)


"""
19. 删除链表的倒数第 N 个结点
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
进阶：你能尝试使用一趟扫描实现吗？
解题思路：快慢指针
希望快指针结束时，慢指针指向倒数第N+1个节点
然后操作第N+1个节点，完成倒数第N个节点的删除操作

需要注意的地方：怎么返回头节点？
一般涉及到头节点变更的问题，都需要借助哑巴节点实现，这里也使用哑巴节点

场景1: 删除的节点就是头节点, n >= 1
可以借助哑巴节点，在头部的前面添加哑巴节点不会影响倒数第N个节点发生变化
    dummy->A->B->None            N = 2
    slow = dummy
    fast = dummy
    for i in range(n+1):
        fast = fast.next
        if fast is None:
            break
    如果链表的长度 == n，也就是说删除的是头部节点
    因为上面的那个循环，是循环了n+1次，所以，fast最终会变成None，而slow不会发生变化
    所以slow.next = slow.next.next 这种调用是安全的

    如果链表的长度 > n，也就是说删除的是中间节点
    因为slow 和 fast中间间隔了n + 1 个节点，而n >= 1, 所以slow 和 fast之间至少隔了两个节点，
    这取决于n的大小
    但是可以肯定的是slow.next = slow.next.next 肯定是安全的 
"""


def kth_node(head: ListNode, n: int) -> ListNode:
    s, f = head, head
    for i in range(n):
        f = f.next

    while f:
        s = s.next
        f = f.next
    return s


def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(-1)
    dummy.next = head

    # 要删除倒数第N个节点，就需要获取倒数第N+1个节点
    # 辅助删除倒数第N个节点
    slow = kth_node(dummy, n + 1)

    slow.next = slow.next.next

    return dummy.next