class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        return removeKdigits(num, k)


"""
特征：非负整数 ，移除k个，最小
解题思路：
   用stack 处理
抽象：
    用stack压入元素
    如果当前元素小于stack[-1]: 弹出stack[-1]
    否则：压入该元素
    k <= 0: break

边界条件：
    k == 0: 返回 num
    num 为空，返回空
    k >= len(num): 返回空
复杂度：
时间复杂度：O(n)
空间复杂度：O(n)
"""


def removeKdigits(num: str, k: int) -> str:
    stack = []
    left_l = len(num) - k
    i = 0
    while i < len(num):
        if stack and stack[-1] > num[i] and k > 0:
            stack.pop()
            k -= 1
        else:
            stack.append(num[i])
            i += 1
    return "".join(stack[:left_l]).lstrip("0") or "0"