 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
> 示例 1:
> 输入: [2,3,-2,4]()
> 输出: 6
> 解释: 子数组 [2,3]() 有最大乘积 6。
> 示例 2:
> 输入: [-2,0,-1]()
> 输出: 0
> 解释: 结果不能为 2, 因为 [-2,-1]() 不是子数组。

```python
class Solution:
    """
    如果 nums[i] 为正数
    max_f(i) = max(max_f(i-1) * nums[i], nums[i])
    如果 nums[i] 为负数
    max_f(i) = max(min_f(i-1) * nums[i], nums[i])
    也就是说：
    max_f(i) = max(max_f(i-1) * nums[i], min_f(i-1) * nums[i], nums[i])
    min_f(i) = min(max_f(i-1) * nums[i], min_f(i-1) * nums[i], nums[i])
    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0: return None
        if len(nums) == 1: return nums[0]
        max_dp = [0] * len(nums)
        min_dp = [0] * len(nums)
        max_dp[0] = nums[0]
        min_dp[0] = nums[0]
        for i in range(1, len(nums)):
            max_dp[i] = max(max_dp[i-1] * nums[i], min_dp[i - 1] * nums[i], nums[i])
            min_dp[i] = min(max_dp[i-1] * nums[i], min_dp[i - 1] * nums[i], nums[i])
        return max(max_dp)

```

