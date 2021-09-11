L20210909 三数之和
```python
class Solution:
    """
    三数之和 - 可以转化为求两数之和
    两数之和的解法有很多种，其中一种就是排序 + 双指针，基于两数之和的这种解法，可以得到三数之和的解法
    难点在于对去重的处理。
    最简单的方式是使用set，之后再将set 转换为list 输出，但是这样会多一次对结果集的遍历
    基于排序之后的数据特征（相等的元素必然相邻），可以实现在遍历的过程中进行去重。
    时间复杂度：O(n^2)
    空间复杂度：O(1)
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if nums[i] > 0: continue # 优化1 ： nums[i] > 0 

            if i > 0 and nums[i] == nums[i - 1]: # 优化2: 去重
                continue
            
            self.twoSum(nums, i + 1, nums[i], ans)
            
        return [item for item in ans]
    
    def twoSum(self, nums: List[int], start: int, target: int, ans) -> List[List[int]]:
        
        left, right = start, len(nums) - 1
        while left < right:
            diff = nums[left] + nums[right] + target
            if diff > 0:
                right -= 1
                # target, nums[left], right
                # 如果 nums[right - 1] == nums[right]，说明 target + nums[left] + nums[right-1] 依然 大于 0
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif diff < 0:
                left += 1
                # 
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
            else:
                ans.append((target, nums[left], nums[right]))
                left += 1
                right -= 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
        return ans
```
