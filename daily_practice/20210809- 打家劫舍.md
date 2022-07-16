20210809- 打家劫舍
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。


```python
class Solution:
    # dp[i] 表示前面i+1家能够偷到的最大值
    # dp[0] = nums[0]
    # dp[1] = max(dp[0], dp[1])
    # dp[i] = max(dp[i-2] + nums[i], dp[i-1])
    # return dp[-1]
    # dp[2] = (dp[1], dp[0] + dp[0])

    # 时间复杂度：O(n)
    # 空间复杂度：O（n)
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2: return max(nums)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            # 取决于前i-2家能获取的最大值 + nums[i]
            # 或者这一家不偷，取决于前i-1家能够获取的最大值
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
            
        return dp[-1]
    # 时间复杂度：O(n)
    # 空间复杂度：O(1)
    # 滚动数组优化版本
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2: return max(nums)
        pre = nums[0]
        cur = max(pre, nums[1])
        for i in range(2, len(nums)):
            tmp = cur
            cur = max(pre + nums[i], cur)
            pre = tmp
        return cur
    
```
