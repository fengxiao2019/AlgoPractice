"""
解题思路：按k个一组进行断开翻转，然后首尾拼接
1. 怎么返回翻转后的头部节点？
    常规的处理方法是定义一个哑巴节点，通过哑巴节点来返回

2. 怎么进行断开后的衔接？
    首尾衔接
3. 最后一组不满k个节点，注意处理衔接问题，不满k个节点，不进行翻转
"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverse_k_group(head: ListNode, k: int) -> ListNode:
    dummy = ListNode(-1)
    dummy.next = head
    pre = dummy

    while head:
        tail = pre
        # 确定第k组的头节点和尾节点,k = 1, 2 ...
        for i in range(k):
            tail = tail.next
            # 因为第57行已经把上一组的tail和这一组的head连接起来了
            # 所以，如果不满足k个元素的情况下，直接返回就ok了
            if tail is None:
                return dummy.next
        # 保存下一个头部节点

        next_head = tail.next
        head, tail = reverse(head, tail)
        # 处理衔接的问题
        pre.next = head  # 将pre 接上翻转后的头部
        tail.next = next_head  # 先把翻转完的接上下一个头节点，方便处理不满k个元素的情况
        head = next_head  # 变更头部为下一组的头部
        pre = tail  # 将pre 设置成翻转后的尾部

    return dummy.next


"""
返回翻转后的 头部节点和尾部节点
注意这里将tail.next 设置成None，这样在才能只翻转head-...-tail
"""
def reverse(head: ListNode, tail: ListNode) -> (ListNode, ListNode):
    prev = None
    # 为了让链表翻转在在尾部结束，需要将tail.next = None
    tail.next = None
    # 用p执行节点的变更操作
    # head 留着返回
    p = head
    while p:
        tmp = p.next
        p.next = prev
        prev = p
        p = tmp

    return prev, head



