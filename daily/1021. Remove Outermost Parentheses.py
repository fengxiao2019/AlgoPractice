class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        return removeOuterParentheses(S)
"""
根据题目表述的意思，第一个"(" 是不能添加的，用balance 记录括号的数量
当banlance == 0 时，说明遇到了一个primitive 括号对，因为第一个"(" 在一开始就没有添加，所以，只需要弹出stack的最后一个元素（也就是“)”）就可以了，
balance 不需要更新，保持0。
处理完字符串中所有的元素，将stack转成字符串就可以了
时间复杂度：O(n)
空间复杂度：O(n)
for item in S:
    while stack and stack[-1] == item:
        stack.pop()
    stack.append(item)
(())
"""
def removeOuterParentheses(s: str) -> str:
    stack = []
    balance = 0
    for item in s:
        if item == '(' and balance > 0: stack.append(item)
        if item == ')' and balance > 1: stack.append(item)
        balance += 1 if item == '(' else - 1
    return "".join(stack)