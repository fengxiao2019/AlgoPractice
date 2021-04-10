"""
138. 复制带随机指针的链表
解题思路：复制每一个节点，存储在该节点之后
eg: 现有链表 
    A->B->C->D->None
复制之后：
    A->A'->B->B'->C->C'->D->D'->None

其中A'是对复制A.val的新节点
这样我们就可以很方便的处理对随机节点的复制
eg: 假设，A.random 指向C，
    我们可以通过A.random.next 得到对random复制的节点
时间复杂度：O(n)
空间复杂度：O(n)
"""


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next


def copy_random_list(head: 'Node') -> 'Node':
    cur = head
    # 先完成复制
    while cur:
        next_node = cur.next
        cur.next = Node(cur.val)
        cur.next.next = next_node
        cur = next_node

    # 构造新链表
    dummy = Node(-1)
    new_head = dummy
    cur = head
    while cur:
        new_node = cur.next
        if cur.random:
            new_node.random = cur.random.next
        new_head.next = new_node
        # 更新new_head
        new_head = new_head.next
        # 更新cur
        cur = cur.next.next
    return dummy.next