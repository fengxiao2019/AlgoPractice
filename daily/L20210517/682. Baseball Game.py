from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        return calPoints(ops)


"""
解题思路：
[5] D => 取stack[-1] * 2, 压入栈    [5, 10]
[5] C => [] stack.pop()
[5 2] + => [5, 2, 7] stack.append(stack[-1] + stack[-2])

边界：
题目中所有操作都确保有效

时间复杂度：O(n)
空间复杂度：O(n)
"""


def calPoints(ops: List[str]) -> int:
    stack = []
    for item in ops:
        if item == 'D':
            stack.append(stack[-1] * 2)
        elif item == 'C':
            stack.pop()
        elif item == '+':
            stack.append(stack[-1] + stack[-2])
        else:
            stack.append(int(item))

    if stack:
        return sum(stack)