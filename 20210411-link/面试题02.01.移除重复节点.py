# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        return remove_duplicate_nodes(head)


"""
面试题 02.01. 移除重复节点
可以使用缓冲区：
因为头节点不会发生变化，所以可以选择不使用虚拟节点
A->B->C->B->B->None

head=A, head本身不会变化
用set 记录已经访问的元素
已经存在的元素就删除，不存在就添加到set中

边界条件检查：空节点和单节点返回
时间复杂度：O(n)
空间复杂度：O(1)
"""


def remove_duplicate_nodes(head: ListNode) -> ListNode:
    if not head:
        return head
    cur = head
    hash_v = set()
    hash_v.add(cur.val)
    # 使用cur.next 是为了便于执行删除
    while cur.next:
        if cur.next.val in hash_v:
            cur.next = cur.next.next
        else:
            cur = cur.next
            hash_v.add(cur.val)
    return head

"""
不可以用缓冲区：双循环
遍历每个节点，嵌套一个循环遍历该节点之后的所有节点，如果有和该节点的值相等的节点就删除
eg: 
1-->2-->3-->3-->2-->1-->None
cur       nxt
1          1.next != 1    => nxt = nxt.next
           2.next != 1    => nxt = nxt.next
           3.next != 1    => nxt = nxt.next
           3.next != 1    => nxt = nxt.next
           2.next == 1    => nxt.next = nxt.next.next 2-1->None ==> 2->None
2          2.next != 2
           3.next != 2
           3.next == 2    =>3->2->1 ==> 3->1->None
           3.next != 1
.....
时间复杂度：O(n^2)
空间复杂度：O(1)
"""
def remove_duplicate_nodes_back(head: ListNode) -> ListNode:
    if not head:
        return None
    cur = head
    while cur and cur.next:
        nxt = cur
        while nxt and nxt.next:
            if nxt.next.val == cur.val:
                nxt.next = nxt.next.next
            else:
                nxt = nxt.next
        cur = cur.next
    return head