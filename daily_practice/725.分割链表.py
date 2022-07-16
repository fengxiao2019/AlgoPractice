from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        return split_list_to_pairs(root, k)


"""
解题思路：
假设链表的长度为l
if l <= k:
    则输出每个节点，不够的返回空
elif k == 1:
    输出整个链表

确定每个组最少的节点数量
min_l = l // k
从头开始可以补齐的节点数量
left_count = l % k 
根据min_l 和 left_count 确定每个组实际的节点数量
if left_count > 0:
    cur_l = min_l + 1
    left_count -= 1
时间复杂度：O(n)
空间复杂度：O(n)
"""


def split_list_to_pairs(root: ListNode, k: int) -> List[ListNode]:
    res = [None] * k
    if k == 1:
        return [root]
    cur = root
    # 计算长度
    count = 0
    while cur:
        cur = cur.next
        count += 1

    min_l = count // k
    left_count = count % k

    cur = root
    index = 0
    while cur:
        cur_l = min_l
        if left_count > 0:
            cur_l += 1
            left_count -= 1
        res[index] = cur

        # A->B->C->D->
        # cur_1 = 1
        for i in range(1, cur_l):
            cur = cur.next
        tmp = cur.next
        cur.next = None
        cur = tmp
        index += 1
    return res