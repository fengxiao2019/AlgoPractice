# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        return next_large_nodes(head)


"""
1019.链表中的下一个更大节点
解题方法：单调递增栈
step1: 先将链表元素在数组中存储
nums: 2->7->4->3->5->None  => [2, 7, 4, 3, 5]
step2: 初始化返回结果res = [0] * len(nums) = [0, 0, 0, 0, 0]
       初始化单调栈stack = [0]

step3: 遍历数组，i in range(1, len(nums))
       逻辑 如果nums[i] > stack顶元素指定的索引在nums中的值

        while stack and nums[i] > nums[stack[-1]]:
            # 更新res
            res[i] = nums[stack[-1]]
            stack.pop()
        stack.append(i)
step4: 返回res

res = []
stack: 0
nums[stack[-1]] < nums[1]: res = [7, 0, 0, 0, 0]   stack = [1]
nums[stack[-1]] > nums[2]: res = [7, 0, 0, 0, 0]   stack = [1, 2]
nums[stack[-1]] > nums[3]: res = [7, 0, 0, 0, 0]   stack = [1, 2, 3]
nums[stack[-1]] < nums[3]: res = [7, 0, 0, 5, 0]   stack = [1, 2]
                           res = [7, 0, 5, 5, 0]   stack = [1]
                           res = [7, 0, 5, 5, 0]   stack = [1, 4]      
时间复杂度：O(n)
空间复杂度：O(n)
"""


def next_large_nodes(head: ListNode) -> List[int]:
    # 处理边界条件
    if not head: return []
    if not head.next: return [0]
    # 构造数组
    nums = []
    cur = head
    while cur:
        nums.append(cur.val)
        cur = cur.next
    # 初始化返回结果
    res = [0] * len(nums)
    # 构造栈
    stack = [0]
    # 开始处理逻辑
    for i in range(1, len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            res[stack[-1]] = nums[i]
            stack.pop()
        stack.append(i)
    return res


"""
暴力解法
固定住一个节点pre，从pre.next开始遍历，找到第一个大于pre.val的值，存储该值，如果没找到append(0)
并且 pre = pre.next，继续执行
时间复杂度：O(n^2)
空间复杂度：O(n)
时间上会被卡住
"""


def next_large_nodes_loop(head: ListNode) -> List[int]:
    # 处理边界条件
    res = []
    if head is None:
        return res
    pre = head
    while pre:
        post = pre.next

        while post:
            if post.val > pre.val:
                res.append(post.val)
                break

            post = post.next
        if post is None:
            res.append(0)
        pre = pre.next
    return res