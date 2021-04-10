"""
2021.04.08
143. 重排链表
解题思路：
step1: 链表从中间断开，左边为l1， 右边为l2
step2: 将l2 进行翻转
step3: 合并l1 和 l2

边界条件处理：
   场景1: head 为空 返回head
   场景2: head.next 为空，返回head
   场景3: head.next.next 为空，eg A->B->None，这样返回的还是A->B->None, 所以返回的还是 head，对于这个场景，后续的处理逻辑也是兼容的
   A->B->None 调用split_link 之后变成
        l1: A->None
        l2: B->None
    对l2翻转之后没有变化，然后合并l1 和 l2，结果没变还是A->B->None


注意的地方：
因为是l0->ln->l1->ln-1-> ...
如果链表的长度n为偶数的话，l1的长度=l2的长度
如果链表的长度n为奇数的话，l1的长度=l2的长度 + 1
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def reorder_list(head: ListNode) -> None:
    if head is None or head.next is None or head.next.next is None:
        return head

    l1, l2 = split_link(head)
    l2 = reverse_link(l2)
    dummy = ListNode(-1)
    new_node = dummy

    while l1 and l2:
        new_node.next = l1
        l1 = l1.next
        new_node.next.next = l2
        l2 = l2.next
        new_node = new_node.next.next

    # 别忘记处理l1
    new_node.next = l1

    head = dummy.next


"""
如何从中间断开链表，保证l1的长度 >= l2的长度
快慢指针法
slow = slow.next
fast = fast.next.next

从上面的语句中可以看出，while 循环的条件 需要判断slow and slow.next and fast and fast.next
因为fast 有效的话，slow节点肯定是有效的，所以循环的条件可以简写为 fast and fast.next

针对偶数长度的链表:
eg: A->B->C->D->None
           step1     step2      step3 
slow:        A         B          C              
faster:      A         C          None
此时，slow的指针指向了C，我们希望在B处断开，所以，在while的循环里面我们添加一个条件，fast.next.next 

合并之后，B必然指向l2的C节点，因此，不处理这种情况，不会影响结果
因为C.next.next 为空，所以退出循环，slow的节点为B，也就是我们期望的l1的尾部节点，slow.next 即为l2的头部节点

针对奇数长度链表:
eg: A->B->C->D->E->None
           step1        step2      step3     step4
slow:        A            B          C         X
faster:      A            C          E         X

因为E.next 为空，不满足while循环的条件，退出循环，此时slow节点为C，也就是我们期望的l1的尾部节点，slow.next 为l2的头部节点

综上所述，我们可以使用快慢指针找到需要的l1 和 l2
时间复杂度：O(n)，假设链表的长度为n，需要遍历n/2个节点
空间复杂度：O(1) 定义了常量个变量
"""


def split_link(head: ListNode) -> (ListNode, ListNode):
    slow = head
    fast = head
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    new_head = slow.next
    slow.next = None
    return head, new_head


"""
翻转链表
时间复杂度：O(n)
空间复杂度：O(1)
"""


def reverse_link(head: ListNode) -> ListNode:
    pre = None
    while head:
        tmp = head.next
        head.next = pre
        pre = head
        head = tmp
    return pre