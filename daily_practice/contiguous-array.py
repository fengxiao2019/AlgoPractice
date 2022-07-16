class Solution:
    """
    0 当成 -1
    1 当称 1
    相当于求和为1的最大连续子子数组
    可以使用前缀和的方法
    下标 0   1   2     3   4   5   6   7
    eg: 0   1    1     1   0   0  0   1
    对应的sum
        -1  0    1     2   1    0 -1  0
    最长为8
    如果sum_val[i] == 0: max_len = max(max_len, i + 1)
    如果 sum_val[i] 为 m, 如果m 存在于sum_hash中，那么，max_len = max(max_len, m - sum_hash[m] + 1)
    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    from typing import List


    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        sum_hash = {}
        sum_v = 0
        max_len = 0
        for i in range(len(nums)):
            sum_v += -1 if nums[i] == 0 else 1
            if sum_v == 0:
                max_len = max(max_len, i + 1)
            elif sum_v in sum_hash:
                max_len = max(max_len, i - sum_hash[sum_v])
            sum_hash.setdefault(sum_v, i)
        return max_len