class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

"""
当要返回倒数第k个节点时，k参数传递 k
当要删除倒数第k个节点时，k参数传递 k + 1
为了统一处理这两种情况，head 需要传递虚拟节点 dummy
# 涉及到的题目：
19. 删除链表的倒数第 N 个结点
剑指 Offer 22. 链表中倒数第k个节点
61. 旋转链表 
    # 旋转k次，k可能大于链表长度，需要先进行 k = k mod len(list) ，然后倒数第k个节点处断开，
    # 传入k+1
    
# 这里没有处理k大于链表长度的问题，一般题目中都明确说明了k的大小
# 但是，面试的时候有可能需要处理一下
"""
def kth_node(head: ListNode, k: int) -> ListNode:
    s, f = head, head

    for i in range(k):
        f = f.next
    # 让f最终指向None节点
    while f:
        f = f.next
        s = s.next

    return s

"""
处理中间节点
题目：876 链表的中间结点 适用类型1  
面试题 02.06	回文链表 适用类型2 
109. 有序链表转换二叉搜索树 适用类型3
"""

"""
类型1： 返回中间靠后的节点
1     2     3  |    4    None     |
f           f  |           f      |
s     s     s  |                  |
从上图中可以看出
如果last_node 在3， s在2处返回   - 奇数个节点
如果last_node 在4， s在3处返回   - 偶数个节点
"""

def mid_node_after(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    s, f = head, head
    while f and f.next:
        s = s.next
        f = f.next.next
    return s

"""
类型2： 返回中间靠前的节点
1     2     3  |    4    None     |
f           f  |           f      |
s     s     s  |                  |
从上图中可以看出
如果last_node 在3， s在2处返回   - 奇数个节点
如果last_node 在4， s在2处返回   - 偶数个节点
"""
def mid_node_before(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    s, f = head, head.next  # 变化的地方 f = head.next
    while f and f.next:
        s = s.next
        f = f.next.next
    return s

"""
类型3： 根据首尾确定中间节点，上面的两种写法是针对一个完整链表求中间节点的
       如果同时指定了head 和 tail 节点，只需要针对上面的两种写法稍微做些调整就可以
eg: 例如下面的这种写法 tail = None 就变成了 mid_node_after
"""

def mid_node(head: ListNode, tail: ListNode) -> ListNode:
    if head == tail or head.next == tail:
        return head
    s, f = head, head
    while f != tail and f.next != tail:
        s = s.next
        f = f.next.next
    return s

"""
翻转链表
通用写法： 接收head 和 tail，前开后闭区间 [head, tail)
eg: A->B->C->D->E->F->None
    翻转B->C->D 这段   head = B, tail = E 
相关题：
206. 翻转链表 
25. K 个一组翻转链表  
剑指 Offer 06 从尾到头打印链表
92 反转链表 II  
面试题 02.06	回文链表  
445	两数相加 II  
143. 重排链表
234	回文链表  
剑指 Offer 06 从尾到头打印链表  
369. 给单链表加一
"""
"""
迭代写法
A->B->C->D->E->None
tail = None

翻转步骤 - 细化

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
    head = head.next

出口条件： head is not None

最后返回pre 就是我们想要的结果
时间复杂度：O(n)  n表示链表的长度
空间复杂度：O(1)  只利用了tmp pre 这两个变量，所以是常数个变量
"""
def reverse(head: ListNode, tail: ListNode) -> ListNode:
    pre = tail
    while head != tail:
        tmp = head.next
        head.next = pre
        pre = head
        head = tmp
    return pre


"""
解题思路
A->B->C->D->E->None
出口条件 node.next is None  因为E.next is None,翻转后的头节点为E
语句1: D.next.next = E
语句2: D.next = None
语句1 和 语句2 可以将 D->E->None  转成 E->D->None

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


def reverse_list_recursion(head: ListNode, tail: ListNode) -> ListNode:
    # not head 可以兼容输入为空节点的情况
    # 出口条件
    if head == tail or head.next == tail:
        return head
    # 递归的执行翻转
    next_node = reverse_list_recursion(head.next, tail)

    # A->B  -->  B->A
    head.next.next = head
    head.next = tail
    # 每次都返回出口条件返回的结果
    return next_node


"""
类型1： k个有序链表的合并 k >= 2

nums = [[1,4,5], [1,3,4], [2,6]]   0     2
left:      start 0  end   1
right:     start 2  end   2  return [2, 6]
left 继续拆分
left_l = start 0  end 0      return [1,4,5] 
left_r = start 1  end 1      return [1,3,4]

开始回归：
left_l  和left_r merge => [1,3,4,4,5]
继续和[2,6] merge
==>  [1,2,3,4,4,5,6]
"""

from typing import List


def merge_list(l1: ListNode, l2: ListNode) -> ListNode:
    """
    两个有序链表的合并
    """
    dummy = ListNode(0)
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


def merge_k_list(lists: List[ListNode], start: int, end: int) -> ListNode:
    """
    k 个有序链表的合并
    """
    if start > end:
        return None
    if start == end:
        return lists[start]

    mid = (start + end) // 2
    left = merge_k_list(lists, start, mid)
    right = merge_k_list(lists, mid + 1, end)
    return merge_list(left, right)

"""
类型2：交叉合并 
l1: A->B->C->D->None
l2: E->F->G->None
l1 merge l2: => A->E->B->F->C->F->D->None
"""
def merge(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(-1)
    new_node = dummy

    while l1 and l2:
        new_node.next = l1
        new_node.next.next = l2

        l1 = l1.next
        l2 = l2.next
        new_node = new_node.next.next

    # 别忘记处理l1
    new_node.next = l1
    return dummy.next

"""
链表去重
"""
def delete_duplicate(head: ListNode) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    head = dummy
    while head and head.next and head.next.next:
        if head.next.val == head.next.next.val:
            to_remove = head.next.val
            while head and head.next and head.next.val == to_remove:
                if head.next.val == to_remove:
                    head.next = head.next.next
            continue
        else:
            head = head.next
    return dummy.next