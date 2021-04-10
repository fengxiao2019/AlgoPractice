
# 206.反转链表
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


"""
解题思路
A->B->C->D->E->None
出口条件 node.next is None  因为E.next is None,翻转后的头节点为E
语句1:D.next.next = D
语句2: D.next = None
语句1 和 语句2 可以将D->E->None  转成 E->D->None

怎么把D.next 变成C？
C.next.next = D
C.next = None 
这样就可以把D.next 变成C了 

以此类推，可以完成E->D->C->B->A->None
总结下语句：
head.next.next = head
head.next = None

怎么返回E呢？
    出口条件处记录了节点E，可以把这个节点作为函数的返回值传回来

时间复杂度：O(n) n 表示链表的长度，递归遍历链表
空间复杂度：O(n) n 表示链表的长度，主要开销是栈的空间
"""


def reverse_list_recursion(head: ListNode) -> ListNode:
    # not head 可以兼容输入为空节点的情况
    # 出口条件
    if not head or head.next is None:
        return head
    # 递归的执行翻转
    next_node = reverse_list_recursion(head.next)

    # A->B  -->  B->A
    head.next.next = head
    head.next = None
    # 每次都返回出口条件返回的结果
    return next_node


"""
A->B->C->D->E->None
可以看成是
翻转后的链表                  翻转前的链表
None                        A->B->C->D->E->None
第一步：A->None              B->C->D->E->None
第二步：B—>A->None           C->D->E->None
第三步：C->B->A->None        D->E->None
第四步：D->C->B->A->None     E->None
第五步：E->D->C->B->A->None  None
完成翻转
从上面的步骤中可以看出
每次执行变更前，需要记住拆开后的两个链表的头部节点
pre 表示翻转后的链表的头节点 
head 表示翻转前的链表的头节点

需要完成下面的变化
    pre = None  head = A
    变成
    pre = A     head = B
    pre = B     head = C
    pre = C     head = D
    pre = D     head = E
    pre = E     head = None

可以通过这种逻辑完成
    tmp = head.next
    head.next = pre
    pre = head
    head = tmp 

出口条件： head is not None

最后返回pre 就是我们想要的结果
时间复杂度：O(n)  n表示链表的长度
空间复杂度：O(1)  只利用了tmp pre 这两个变量，所以是常数个变量
"""


def reverse_list_iteration(head: ListNode) -> ListNode:
    pre = None
    while head is not None:
        tmp = head.next
        head.next = pre
        pre = head
        head = tmp
    return pre