53. 最大子序和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
	
```python
class Solution:
	"""
	暴力解法：n^2 
	优化解法：f(i) 表以i结尾的子数组构成的最大自序和
	f(i) = max(f(i-1) + nums[i], nums[i])
	max_val = max(max_val, f(i))
	return max_val
	时间复杂度：O(n)
	空间复杂度：O(n)
	"""
	def maxSubArray(self, nums: List[int]) -> int:
    	if not nums: return 0
    	max_val = nums[0]
    	dp = [0] * len(nums)
    	dp[0] = nums[0]
    	for i in range(1, len(nums)):
        	dp[i] = max(dp[i-1] + nums[i], nums[i])
        	max_val = max(max_val, dp[i])
    	return max_val

	"""
	优化空间复杂度到O(1)
	滚动数组的方式
	因为dp[i] 只和dp[i-1]有关系，所以我们可以用一个变量记录dp[i-1]
	这样就不需要dp这个数组了
	空间复杂度可以将到O(1)
	"""
	def maxSubArray(self, nums: List[int]) -> int:
    	if not nums: return 0
    	max_val = nums[0]
    	pre_val = nums[0]
    	for i in range(1, len(nums)):
        	cur_val = max(pre_val + nums[i], nums[i])
        	max_val = max(max_val, cur_val)
        	pre_val = cur_val
    	return max_val
```

	    	
