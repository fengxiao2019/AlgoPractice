"""
(ed(et(oc))el)
解题思路：
这个题可以利用stack来解决
具体思路：
观察(ed(et(oc))el) 的执行步骤：
(ed(et(oc))el) => (ed(etco)el) => (edocteel) => leetcode

抽象：
用stack 不断压入string 字符，遇到右括号：弹出字符直到左括号。
eg: 最里面的子串(oc) => 弹出后变成：co，把该字符串再逐个压入到stack中。
重复上述过程

边界条件处理：
空串： 也不需要处理了，直接返回空串
没有大括号：满足上述的抽象过程

复杂度：
时间复杂度：O(n)
空间复杂度：O(n)
"""
from typing import List


def reverseParentheses(s: str) -> str:
    stack = []
    tmp_arr = []
    # 开始遍历
    for item in s:
        if item == ")":
            stack.extend(reversedSubStr(stack))
        else:
            stack.append(item)
    return "".join(stack)


# 获取单个括号内的子串
def reversedSubStr(stack: List[str]):
    ans = []
    while stack:
        peek = stack.pop()
        if peek == '(':
            break
        else:
            ans.append(peek)
    return ans
