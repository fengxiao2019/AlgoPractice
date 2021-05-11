#https://leetcode-cn.com/problems/build-an-array-with-stack-operations/

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        return buildArray(target, n)


"""
思路：
找stack 和 list的关系
1  i 相等 => push
1  i 不等 => push pop
怎么退出呢？
完善上面两个步骤
j 表示stack的下标
i 表示 1...n
i == stack[j] => push
i < stack[j] => push pop
i > stack[j] => break
时间复杂度：O(n)
空间复杂度：O(n)
"""

from typing import List
def buildArray(target: List[int], n: int) -> List[str]:
    j = 0
    ans = []
    for i in range(1, n + 1):
        if j >= len(target):
            break

        if i == target[j]:
            ans.append('Push')
            j += 1
        elif i < target[j]:
            ans.append('Push')
            ans.append('Pop')
        else:
            break
    return ans
