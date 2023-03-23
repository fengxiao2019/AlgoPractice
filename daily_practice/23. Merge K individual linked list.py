"""
2021.04.08
23. 合并K个升序链表
解题思路：merge sort 的思想
eg
[1->4->5, 1->3->4, 2->6]
   [1->4->5, 1->3->4]    [2->6]
   [1->4->5]  [1->3->4]  [2->6]
   [1->3->4->4->5]       [2->6]
   [1->2->4->4->5->6]

再详细一点
nums = [[1,4,5], [1,3,4], [2,6]]   start=0    end=2
left:      start 0      end   1
right:     start 2      end   2  return [2, 6]

left 继续拆分
left_l = start 0  end 0          return [1,4,5]
left_r = start 1  end 1          return [1,3,4]

开始回归：
left_l  和left_r merge => [1,3,4,4,5]
继续和[2,6] merge
==>  [1,2,3,4,4,5,6]
时间复杂度：O(knlogk) n 表示单个链表的平均长度
"""

from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_list(l1: ListNode, l2: ListNode) -> ListNode:
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
    if start > end:
        return None
    if start == end:
        return lists[start]

    mid = (start + end) // 2
    left = merge_k_list(lists, start, mid)
    right = merge_k_list(lists, mid + 1, end)
    return merge_list(left, right)

from collections import defaultdict