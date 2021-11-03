from typing import List
class Solution:
    """
    假设用dp[i] 表示以nums[i-1]为最后一个元素构成有序序列的最大长度
    如果有 nums[j] > nums[i], dp[j] = dp[i] + 1
    最后求出dp中最大的值就是想要的结果
    时间复杂度：O(n^2)
    空间复杂度：O(n)
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)
