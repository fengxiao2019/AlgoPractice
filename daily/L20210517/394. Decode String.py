class Solution:
    def decodeString(self, s: str) -> str:
        return decodeString(s)
from typing import List

"""
解题思路：
    用栈处理

抽象过程：
    3[a]2[bc]
    step1: 怎么找到3这个数字的作用范围？[a]
        当我遇到"]" 时，开始出栈操作，直到"[",这样得到了要复制的字符串
    怎么找到要重复多少次？
        在step1 结束后，继续 出栈操作，直到弹出的字符不在'0' - '9'范围内，将数字转化为整数
        把复制后结果集加入到栈中，继续重复step1
    这样，最后stack中存储的结果就是decode的结果，将结果转化为字符串
边界条件处理：
    空串： 空
    没有n[] 这种：抽象逻辑满足这种
    字符串是否都是有效的？有效的
时间复杂度：
    Time complexity: O(n)
    Space Complexity: O(n)
"""


def decodeString(s: str) -> str:
    if not s: return ""
    stack = []
    # 定义结果集
    ans = []
    for item in s:
        if item == ']':
            # 获取字符串列表
            strArr = getCharacters(stack)
            # 获取数字
            count = getNumber(stack)
            # 重新入栈
            for i in range(count):
                for char in strArr:
                    stack.append(char)
        else:
            stack.append(item)
    return "".join(stack)


def getNumber(stack: List[int]) -> int:
    strVal = ""
    while stack and '0' <= stack[-1] <= '9':
        strVal = stack.pop() + strVal
    if not strVal: return 1
    return int(strVal)


def getCharacters(stack: List[int]) -> List[str]:
    ans = []
    while stack:
        peek = stack.pop()
        if peek == '[':
            break
        ans.append(peek)
    return ans[::-1]