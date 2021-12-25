"""
题目：
Given an array of integers nums containing n + 1 integers
# where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
"""

"""
[1,3,4,2,2] =>
[1, 2, 2, 2, 4] 只有一个重复
 0  1  2  3  4
 下标 mid 上的元素应该是mid + 1
 l < r:
 i >= nums[i]: 在左边，r = i - 1

 i == nums[i] - 1: 在右边：l = mid + 1
 返回nums[l]
 时间复杂度：O(nlogn)
 空间复杂度：O(1)
"""


from typing import List
def findDuplicate(nums: List[int]) -> int:
    nums.sort()
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if mid >= nums[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return nums[l]