class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return backspace(s) == backspace(t)
from typing import List
"""
因为‘#’ 涉及到删除操作，所以可以使用stack模拟这种操作
eg: ab#c => [a] => 遇到b=> [ab] => 遇到# => [a] => 遇到c => [ac]
ad#c => [a] => [ad] => [a] => [ac]
时间复杂度：O（max(len(s), len(t))
空间复杂度：O(max(len(s), len(t))
"""

def backspace(s: str) -> List[str]:
    stack = []
    for item in s:
        if item == '#':
            if stack: stack.pop()
        else:
            stack.append(item)
    return stack

"""
转换成数组进行操作，用下标模拟栈的操作
时间复杂度：O(m + n)
空间复杂度：O(m + n)
"""
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return backspace([item for item in s]) == backspace([item for item in t])


def backspace(arr: List[str]) -> List[str]:
    i = 0
    for j in range(len(arr)):
        if arr[j] != '#':
            arr[i] = arr[j]
            i += 1
            j += 1
        else:
            if i > 0: i -= 1
    return arr[:i]