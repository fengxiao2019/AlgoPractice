"""
2021.04.08
19. 删除链表的倒数第 N 个结点
解题思路：快慢指针
希望快指针结束时，慢指针指向倒数第N+1个节点
然后操作倒数第N+1个节点，完成倒数第N个节点的删除操作

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
场景2: 删除的节点是中间节点
    场景1中的算法依然满足这个场景
时间复杂度：O(n) n 为链表的长度， 遍历了n+1次，fast节点从哑巴节点移动到结尾，所以时间复杂度为O(n)
空间复杂度：O(1) 只定义了常量个变量，所以空间复杂度为O(1)
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(-1)
    dummy.next = head

    slow, fast = dummy, dummy
    for i in range(n + 1):
        fast = fast.next
        if not fast:
            break

    while fast:
        fast = fast.next
        slow = slow.next

    """ 
    如果链表的长度 == n，也就是说删除的是头部节点
    因为上面的那个for循环(35-38行)，是循环了n+1次，所以，fast最终会变成None，而slow不会发生变化
    所以slow.next = slow.next.next 这种调用是安全的
    就算n为1，slow 因为指向的是dummy，所以slow.next.next 也是安全的

    如果链表的长度 > n，也就是说删除的是中间节点
    因为slow 和 fast中间间隔了n + 1 个节点，而n >= 1, 所以slow 和 fast之间至少隔了两个节点
    可以肯定的是slow.next = slow.next.next 肯定是安全的 
    """
    slow.next = slow.next.next

    # 这里返回哑巴节点指向的下一个节点
    return dummy.next