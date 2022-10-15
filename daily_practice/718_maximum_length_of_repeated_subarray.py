"""
title 最长重复子数组
给两个整数数组 nums1 和 nums2 ，返回 两个数组中 公共的 、长度最长的子数组的长度 。

示例 1：

输入：nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
输出：3
解释：长度最长的公共子数组是 [3,2,1] 。
示例 2：

输入：nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
输出：5

提示：
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 100

"""

from typing import List

"""
dp problem
dp[i][j] is the longest common suffix between nums1[0: i] and nums2[0: j]
time complexity: O(m * n) 
the space complexity: O(m * n)

    1 ---- 2  ---- 3 ---- 4  ---- 5 --- 6
4   0      0       0      1       0     0
|   
|
5   0      0       0      0       2     0
|
|
6   0      0       0      0       0     3
|
|
1   1      0       0      0       0     0
|
|
2   0      1       0      0       0     0
"""

def findLength(nums1: List[int], nums2: List[int]) -> int:
    # dpp[i][j] means the length of repeated subarray of nums1[0:i] and nums2[:j]
    # so if nums1[i] == nums2[j] --> dp[i][j] = dp[i + 1][j+1]
    dp = [ [0] * (len(nums2) + 1) for i in range(len(nums1) + 1) ]
    max_val = 0
    for i in range(1, len(nums1) + 1):
        for j in range(1, len(nums2) + 1):
            dp[i][j] = dp[i - 1][j - 1] + 1 if nums1[i - 1] == nums2[j - 1] else 0
            max_val = max(dp[i][j], max_val)
    return max_val


ans = findLength([1,2,3,2, 1], [3, 2, 1, 4, 7])
print(ans)




