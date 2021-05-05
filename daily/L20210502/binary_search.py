from typing import List
import unittest
#剑指 Offer 53 - II. 0～n-1中缺失的数字
# 一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。
# 在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

"""
如果不缺失的话，下标和对应下标的值是相等的
所以
if mid == nums[mid]:  l = mid + 1
else: r = mid - 1
时间复杂度：O(logn)
空间复杂度：O(1)
"""

def missingNumber(nums: List[int]) -> int:
    l, r = 0, nums[-1]
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == mid: l = mid + 1
        else: r = mid - 1
    return l


class TestMissNumber(unittest.TestCase):
    def test_one(self):
        arr = [1]
        self.assertEqual(missingNumber(arr), 0)

    def test_lastone(self):
        arr = [0, 1, 2, 3]
        self.assertEqual(missingNumber(arr), 4)

    def test_midone(self):
        arr = [0, 2, 3]
        self.assertEqual(missingNumber(arr), 1)


"""
34. 在排序数组中查找元素的第一个和最后一个位置
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回[-1, -1]。
进阶：
你可以设计并实现时间复杂度为O(log n)的算法解决此问题吗？
"""

"""
找应当插入的位置
eg: [5, 7, 7, 8, 8, 10]  target = 8  返回3  target = 9 返回 5
              ^
时间复杂度：O(logn)
空间复杂度：O(1)
"""
def searchRange(nums: List[int], target: int) -> List[int]:
    l, r = 0, len(nums)

    while l < r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid
    return l


"""
找最右边
[5, 7, 7, 8, 8, 10] target = 8 返回的是元素10 的下标
"""
def searchRange(nums: List[int], target: int) -> List[int]:
    l, r = 0, len(nums)
    while l < r:
        mid = (l + r) // 2
        if nums[mid] > target:
            r = mid
        else:
            l = mid + 1

    return l
