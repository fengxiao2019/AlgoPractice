"""
解题思路：扩展nums为 nums + nums，这样每个元素都能够找到比他大的下一个元素
res = [-1] * len(nums)
这样，我们不用处理找不到比当前元素大的元素
对于扩展后的下标：对应的实际下标为 i % len(nums)
为了找到比当前元素大的下标，实际上是在维护一个递减栈
时间复杂度：O(n)
空间复杂度：O(n)
"""

from typing import List
def nextGreaterElements(nums: List[int]) -> List[int]:
    length = len(nums)
    nums = nums + nums
    res = [-1] * length
    stack = []
    for i in range(length + length):
        while stack and nums[stack[-1]] < nums[i]:
            val = stack.pop()
            res[val] = nums[i]
        stack.append(i % length)

    return res