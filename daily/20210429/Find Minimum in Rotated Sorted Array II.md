154. Find Minimum in Rotated Sorted Array II
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:

[4,5,6,7,0,1,4] if it was rotated 4 times.
[0,1,4,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

154. 寻找旋转排序数组中的最小值 II  
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。

**解题方法1: 二分查找**
```python
"""
二分查找
3   4    5   1   2
l        m       r
if numbers[m] < numbers[r]:
      
说明在m在右边部分，最小值在左边：r = m，有可能是m对应value本身

if numbers[m] > numbers[r]:
    5         >   2
    说明m在左半边，最小值在右边 l = m + 1

if numbers[m] == numbers[r]: 
    无法判断：因为有重复元素，所以，r = r - 1是安全的，不会丢掉可能的值
时间复杂度：O(logn)
空间复杂度：O（1）
"""

def minArray(numbers: List[int]) -> int:
    # 检查入口参数
    if not numbers: return None
    if len(numbers) == 1: return numbers[0]
    l,r = 0, len(numbers) -1
    # [3,1,2]
    # l 0  r 4
    while l < r:
        m = (l + r) // 2
        if numbers[m] > numbers[r]:
            # 说明m在左边有序部分, 并且numbers[m] 本身不是最小值
            l = m + 1
        elif numbers[m] < numbers[r]:
            # 说明m在右边有序部分
            r = m
        else:
            # 无法判断的情况
            r -= 1
    return numbers[l]


```

**解题方法2:双指针 模拟旋转**
```python
"""
解题思路：模拟旋转
3 4 5 1 2
l_val = 3   r_val = 2
如果l_val < r_val: 说明已经有序，直接返回最小值l_val
否则：模拟一次旋转，让l_val = r_val, r = r - 1
直到l_val < r_val 

重复元素的处理：l_val == r_val，说明对r_val 是否模拟旋转并不重要，
直接让r -= 1就可以了，然是如果所有元素都相等，就存在找不到的情况，所以，最后返回l_val 就可以满足全是重复的情形。

时间复杂度：O(n)
空间复杂度：O（1)
"""

def minArray(numbers: List[int]) -> int:
    if not numbers: return None
    if len(numbers) == 1: return numbers[0]

    r = len(numbers) - 1
    l_val = numbers[0]
    while r >= 0:
        # 已经是有序了，返回l_val
        if l_val < numbers[r]:
            return l_val
        elif l_val > numbers[r]:
            l_val = numbers[r]
            r -= 1
        else:
            r -= 1
    return l_val
```

**解题方法2: 二分查找- mid 和左边值比较**
```python
"""
二分查找以左边和mid 比较
关键在于用min_v 记录每一次迭代过程中可能出现最小值
"""
def minArray(nums: List[int]) -> int:
    min_v = nums[0]
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == nums[l]:
            min_v = min(min_v, nums[mid])
            l += 1
        elif nums[mid] > nums[l]:
            min_v = min(min_v, nums[l])
            l = mid + 1
        else:
            min_v = min(min_v, nums[mid])
            r = mid - 1
    return min_v
"""
```
