"""
2021.04.08
153.寻找旋转排序数组中的最小值
解题思路：二分查找
旋转之后，任意索引i 都将数据分成两部分
left = nums[:i]     right=nums[i:]
假设min_v = nums[0]
因为无重复数据，所以必然有一部分是有序的,假设有序是从start节点开始的
min_v = min(min_v, nums[start])
继续搜索另一半， 重复上面的步骤

以一个例子说明：
假设min_v = nums[0] = 4
eg: 4   5   6    7    0   1   2
    0   1   2    3    4   5   6
start         end           mid        min_v
0               6            3           4
4               6            5           0 = min(4, 0)
6               6            6           0 = min(0, 2)
7               6      break
找到最小值为0

边界处理
    数组只有一个元素
        reuturn nums[0]
"""
from typing import List


def find_min(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    min_v = nums[0]
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2

        # bug：别忘记处理边界条件 <=
        # mid 可能和start 相等
        if nums[start] <= nums[mid]:
            min_v = min(nums[start], min_v)
            start = mid + 1
        else:
            min_v = min(nums[mid], min_v)
            end = mid - 1
    return min_v