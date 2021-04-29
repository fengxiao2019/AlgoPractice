# %%

"""
prob: 有思路，但是没有具体化，在实现的过程中容易翻车
"""
class SNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return f"<Node> {self.value}"

    def insert(self, value):
        self.next = SNode(value)
        return self.next

"""
定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
示例 1:
输入: 1->1->2
输出: 1->2

示例 2:
输入: 1->1->2->3->3
输出: 1->2->3
"""



def delete_duplicates(head):
    current = head
    while current:
        if current.next and current.next.value == current.value:
            current.next = current.next.next
        else:
            current = current.next
    return head


def test_d_d():
    list_v = SNode(12)

    delete_duplicates(list_v)
    n = list_v
    while n:
        print(n.value)
        n = n.next
test_d_d()
        
# %%
"""
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
示例 1:
输入: 1->2->3->3->4->4->5
输出: 1->2->5

示例 2:
输入: 1->1->1->2->3
输出: 2->3
"""


def del_duplicate(head):
    dummy = SNode(-1)
    dummy.next = head
    head = dummy
    while head.next and head.next.next:
        if head.next.value == head.next.next.value:
            rm_v = head.next.value # 记录已经被删除的值
            while head.next.value == rm_v:
                head.next = head.next.next
        else:
            head = head.next
    return dummy.next


"""
翻转单向链表
"""


def reverse_slist(head):
    if head.next is None:
        return
    current = head.next
    while current.next:
        tmp = current.next
        current.next = tmp.next
        tmp.next = head
        head = tmp
    return head


def reverse_slist_1(head):
    prev = None
    while head:
        tmp = head.next
        head.next = prev
        prev = head
        head = tmp
    return prev


"""反转从位置 m 到 n 的链表。请使用一趟扫描完成反转"""


def reverse_slist_mn(head, m, n):
    prev = None
    i = 0
    current = head
    while i < m:
        prev = current
        current = current.next
        i += 1

    j = i
    next_n = None
    mid = current
    while current and j <= n:
        tmp = current.next
        current.next = next_n
        next_n = current
        current = tmp

    prev.next = next_n
    mid.next = current
    return head


"""
将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
"""
def merge_two_sorted_list(l1, l2):
    dummy = SNode(None)
    head = dummy
    while l1 and l2:
        if l1.value > l2.value:
            head.next = l2
            l2 = l2.next
        else:
            head.next = l1
            l1 = l1.next
        head = head.next
    while l1:
        head.next = l1
        l1 = l1.next
        head = head.next
    
    while l2:
        head.next = l2
        l2 = l2.next
        head = head.next

    return dummy.next


"""
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
"""


def partion_list(head, x):
    if head is None:
        return

    greater_dummy = SNode(None)
    head_dummy = SNode(None)
    head_dummy.next = head
    g_head = greater_dummy
    head = head_dummy
    while head.next:
        if head.next.value < x:
            head.next = head.next.next
        else:
            g_head.next = head.next
            head.next = head.next.next
            g_head = g_head.next
    g_head.next = None
    head.next = g_head.next
    return head_dummy.next

"""
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
"""
def sort_list(head):
    return merge_sort(head)


def find_middle(head):
    slow = head
    fast = head.next
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow


def merge_sort(head):
    middle = find_middle(head)
    tail = middle.next
    middle.next = None
    left = merge_sort(head)
    right = merge_sort(tail)
    result = merge_two_sorted_list(left, right)
    return result


"""
给定一个单链表 L：L→L→…→L__n→L 将其重新排列后变为： L→L__n→L→L__n→L→L__n→…
思路：找到中点断开，翻转后面部分，然后合并前后两个链表
"""
def reorder_list(head):
    middle = find_middle(head)
    tail = middle.next
    middle.next = None
    reversed_head = reverse_slist(tail)
    current = head
    while head and reversed_head:
        tmp = head.next
        head.next = reversed_head
        head.next.next = tmp.next

        reversed_head = reversed_head.next
        head = tmp.next
    return current


"""
给定一个链表，判断链表中是否有环。
"""
def check_loop(head):
    if not head:
        return False

    slow = head
    fast = head.next
    while fast and slow != fast:
        slow = slow.next
        fast = fast.next.next if fast.next else None
    return False if fast is None else True


"""
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
"""
def loop_first_node(head):
    if not head:
        return False
    slow = head
    fast = head.next
    while fast:
        if slow == fast:
            break
        else:
            slow = slow.next
            fast = fast.next.next if fast.next else None
    if not fast:
        return None
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow
"""
请判断一个链表是否为回文链表。
先找到链表的中间节点
"""
def palindrome_link(head):
    # find the middle
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    cur = slow.next
    slow.next = None
    # reverse fast
    pre = None
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    
    while pre and head:
        if pre.node != head.node:
            return False
        else:
            pre = pre.next
            head = head.next
    return True

"""
给定一个链表，每个节点包含一个额外增加的随机指针，
该指针可以指向链表中的任何节点或空节点。 要求返回这个链表的 深拷贝。
"""
# 问题的难点如何将随机指针copy

def deep_copy(head):
    # copy
    cur = head
    while cur:
        tmp = cur.next
        cp_cur = SNode(cur.value)
        cp_cur.next = cur.next
        cur.next = cp_cur
        cur = tmp 
    
    # process random
    cur = head
    while cur and cur.next:
        # don't froget to process the empty pointer
        if cur.random:
            cur.next.random = cur.random.next
        cur = cur.next.next
    
    # split slink
    cur = head
    new_head = cur.next
    while cur and cur.next:
        tmp = cur.next
        cur.next = cur.next.next
        cur = tmp
    return new_head
