from typing import List
import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        return evalRPN(tokens)


"""
解题思路：用栈
入栈：数字入栈
碰到运算符：弹出两个数
val1 = stack.pop()
val2 = stack.pop()
根据运算符做计算，计算之后重新压入栈中
时间复杂度：O(1)
空间复杂度：O(1)
"""


def evalRPN(tokens: List[str]) -> int:
    stack = []
    for item in tokens:
        if item in ('+', '-', '*', '/'):
            val1 = stack.pop()
            val2 = stack.pop()
            if item == '+':
                stack.append(val1 + val2)
            elif item == '-':
                stack.append(val2 - val1)
            elif item == '*':
                stack.append(val1 * val2)
            else:
                stack.append(int(operator.truediv(val2, val1)))
        else:
            stack.append(int(item))
    if stack:
        return stack[-1]
