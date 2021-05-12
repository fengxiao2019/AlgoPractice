
"""
思路：
可以利用stack解决该问题

[73, 74, 75, 71, 69, 72, 76, 73]

抽象：
结果集为 [0] * len(temperatures)
stack 存储下标，默认为[]
当前温度比stack顶下标指向的温度高：更新结果集中对应下标 val：cur - stack[-1]

边界条件检查：
温度为空： 空
温度长度为1: [0]
检查抽象过程是否能够覆盖这两个边界条件

复杂度：
时间复杂度：O(n)
空间复杂度：O(n)
"""
from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    ans = [0] * len(temperatures)
    stack = []
    i = 0
    while i < len(temperatures):
        if stack and temperatures[i] > temperatures[stack[-1]]:
            peek = stack.pop()
            ans[peek] = i - peek
        else:
            stack.append(i)
            i += 1
    return ans