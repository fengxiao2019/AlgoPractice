26. 删除有序数组中的重复项
**描述**
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
**解题思路**
```python
解题思路：利用双指针
i, j = 0, 1 
if nums[i] == nums[j]: j += 1; 
else: nums[i + 1] = nums[j];    i += 1; j += 1
return i + 1 
```
**代码**
```python
def remove_duplicates(nums: List[int]) -> int:
    if not nums or len(nums) == 1: return len(nums)
    length = len(nums)
    i, j = 0, 1
    while j < length:
        if nums[i] != nums[j]:
            nums[i + 1] = nums[j]
            i += 1
        j += 1
    return i + 1
```
