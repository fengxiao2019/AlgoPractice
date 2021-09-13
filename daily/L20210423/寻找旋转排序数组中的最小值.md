153. 寻找旋转排序数组中的最小值

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        旋转之后必然存在一个有序区间。
        如果旋转之后：和原数组一致，return nums[0]
        如果 nums[left] > nums[mid]:
            说明 nums[mid] -- nums[right] 区间有序
            right = mid
        如果nums[left] < nums[mid]:
            说明nums[left] -- nums[mid]区间有序
            因为一开始排除了left-right区间有序的场景，所以可以确定nums[left]不是最小值
            left = mid + 1
        
        时间复杂度：O(logn)
        空间复杂度：O(1)
        """
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            if nums[left] < nums[right]:
                return nums[left]
            
            mid = left + (right - left) // 2
            if nums[left] > nums[mid]:
                right = mid
            else:
                left = mid + 1
        return min(nums[left], nums[right])
```

154. 寻找旋转排序数组中的最小值 II
```python
class Solution:
    """
    有了重复数字之后，为什么会影响153题的逻辑？
    在没有重复数字的时候，可以根据nums[left] 和 nums[mid]之间的先后顺序，确定有序空间
    但是，如果有重复数字，无法简单根据比大小判断升序区间的位置
    例如：
    2  2   2   0    1

    l      m
    nums[l] >= nums[m] => 升序区间在哪里？153题的判断是在m的右边，小数据在右边，显然是有问题的
    需要额外做去重处理
    时间复杂度：O（n)
    空间复杂度：O(1)
    """
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[left] < nums[right]: return nums[left]
            if nums[left] == nums[right]:
                left += 1
            elif nums[left] > nums[mid]: # 严格有序
                right = mid
            else:
                left = mid + 1
        return min(nums[left], nums[right])
```
