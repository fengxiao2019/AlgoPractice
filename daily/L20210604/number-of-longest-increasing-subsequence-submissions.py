from typing import List
class Solution:
    """
           1    3      5     4      7
    len    1    2      3     3      4

    cnt    1    1      1     1      2
    对于第i个元素，j 属于0, 1, 2, ....,i-1
    length[i] 代表以下标i结束构成的最长递增子序列
    cnt[i] 表示以下标i结束构成的最长递增子序列的个数

    如果 nums[i] > nums[j]，因为length[j] 表示以下标j结尾的最长递增子序列的长度，所以，我们可以得出
        lenght[i] = length[j] + 1
        如何更新cnt的值？
        如果length[i] == length[j] + 1 更新cnt[i]的值

    时间复杂度：O(n ^ 2)
    空间复杂度：O(n)
    """

    def findNumberOfLIS(self, nums: List[int]) -> int:
        length = [0] * len(nums)
        cnt = [0] * len(nums)
        for i in range(len(nums)):
            cnt[i], length[i] = 1, 1
            for j in range(i):
                if nums[i] > nums[j]:
                    if length[i] == length[j] + 1:
                        cnt[i] += cnt[j]
                    elif length[i] < length[j] + 1:
                        cnt[i] = cnt[j]
                        length[i] = length[j] + 1

        # 获取length中最长的递增子序列的长度
        ans = 0
        max_len = max(length)
        for i in range(len(length)):
            if length[i] == max_len:
                ans += cnt[i]
        return ans
