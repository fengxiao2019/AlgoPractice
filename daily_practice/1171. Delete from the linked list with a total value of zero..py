# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        return remove_zero_sum_sublists(head)


"""
1171. 从链表中删去总和值为零的连续节点
A->B->C->D->E->F->D->None
原理：如果A->...->F sum 为 100
     并且A->...->C sum 为 100
     说明D->...->F sum 为 0

     2. 在遍历节点不断推进的过程中，sum相同的节点会被后面的节点覆盖
    0   1   2    3    4   5    6
eg: 1-->2-->3-->-3-->-2-->3-->-3
sum 1   3   6    3    1   4    1

hash = {1: 6, 3: 3, 6: 3, 4: 4}

第一个节点的sum 等于最后一个节点的sum，第二次遍历仅仅执行了第一个节点就完成了

一次遍历获取截止到每个节点的sum，key 为sum，value 为 node
再进行一次遍历，利用上面的原理，获得sum 为0的区间，删除

注意事项：头节点可能会被删除，所以需要建立value 为0的虚拟节点
时间复杂度：O(n)
空间复杂度：O(n) 
"""


def remove_zero_sum_sublists(head: ListNode) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    cur = dummy
    sum_v = 0
    sum_hash = {}
    while cur:
        sum_v += cur.val
        sum_hash[sum_v] = cur
        cur = cur.next

    cur = dummy
    sum_v = 0
    while cur:
        sum_v += cur.val
        if sum_v in sum_hash:
            cur.next = sum_hash[sum_v].next
        cur = cur.next
    return dummy.next