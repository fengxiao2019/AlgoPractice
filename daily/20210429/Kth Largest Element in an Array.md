215. Kth Largest Element in an Array
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

215. 数组中的第K个最大元素
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
```python
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```

**解题方法1: 快排**
```python
"""
解题思路: 快排思想
3212 5 768
     ^
第4 大的元素是5， 我并不需要关心数组是否排序，我只需要确认5 左边的元素都比它小，右边的元素都大于等于它，这就可以用到快排的思想。
时间复杂度：O(n)
空间复杂度：O(logn)
"""
```
**代码**
```python
def findKthLargest(nums: List[int], l: int, r: int, k: int) -> int:
    # 退出条件
    if r - l <= 1:
        return nums[l]
    
    mid = partion(nums, l, r)
    if mid + k == len(nums):
        return nums[mid]
    elif mid + k > len(nums):
        return findKthLargest(nums, l, mid, k)
    else:
        return findKthLargest(nums, mid + 1, r, k)


def partion(nums: List[int], l: int, r: int) -> int:
    pos = r - 1
    pivot = nums[pos]
    j = pos - 1
    i = l

    while i <= j:
        if nums[j] >= pivot:
            nums[pos] = nums[j]
            pos -= 1
            j -= 1
        else:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[pos] = pivot
    return i
```

**解题方法2: 小顶堆**
```python
"""
解题思路：利用小顶堆
时间复杂度：O(nlgk)
空间复杂度：O(k)
"""

def findKthLargest(nums: List[int], k: int) -> int:
    if len(nums) < k: return None
    heap = []
    heapq.heapify(heap)
    for item in nums:
        heapq.heappush(heap, item)
        if len(heap) > k:
            heapq.heappop(heap)
    if not heap: return None
    res = heapq.heappop(heap)
    return res
```
