
from typing import List
"""
如果你要从循环内部返回匹配结果，你可以使用 while (start <= end) 。
如果你想先退出循环，然后使用start或end的结果来返回匹配，你可以使用 while (start < end)。
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            # 这里先判断mid  和 r ，如果反过来就不对了
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[l]