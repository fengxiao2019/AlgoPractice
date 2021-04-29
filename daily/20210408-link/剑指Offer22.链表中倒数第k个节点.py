"""
剑指 Offer 22. 链表中倒数第k个节点
解题思路： 快慢指针
思想：希望快指针结束时，慢指针刚好在倒数第k个节点上
1. 定位 slow 为head, slow = head, f = head
2. 确定 fast 指针: for i in range(k): f = f.next , 但是要注意处理边界条件
3. 同时前进快慢指针，步长都为1，当快指针结束时，慢指针就倒数第k个

# 如果是要删除倒数第 k个节点，就是要找到倒数第k+1个节点
# for i in range(k + 1): f = f.next
eg: A-->B-->C-->D-->E-->F-->G-->H-->I-->None       k = 3  G节点

    slow        fast
      G           None
      F            I
      E            H
      D            G
      C            F
      B            E
      A            D

所以我希望当slow 是A节点时，fast在D节点
fast = A                假如前面有哑巴节点     fast = dummy    需要range(k)
i   fast                                 i         fast
0     B                                  0           A
1     C                                  1           B
2     D                                  2           C
3     break                              3           break
range(k)
要是删除第k个节点                               要是删除第k个节点，需要k+1
需要 range(k+1)                                   range(k+1)
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def get_kth_from_end(head: ListNode, k: int) -> ListNode:
    slow, fast = head, head
    for i in range(k):
        if not fast:
            return None
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    return slow
