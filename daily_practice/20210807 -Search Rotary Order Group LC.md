20210807 - 搜索旋转有序数组 LC
> 整数数组 nums 按升序排列，数组中的值 互不相同 。

> 在传递给函数之前，nums 在预先未知的某个下标 k（0 \<= k \< nums.length）上进行了 旋转，使数组变为 [nums\[k](), nums[k+1](), ..., nums[n-1](), nums[0](), nums[1](), ..., nums[k-1]()]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7]() 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2]() 。
> 
> 给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

```go
// 数组中的值互不相同
// 时间复杂度：O(logn)
// 关键在于明确 必然有一边是有序的，target 在有序的部分，不在有序的部分
func search(nums []int, target int) int {
    left, right := 0, len(nums) - 1
    for left <= right {
        var mid = left + (right - left) / 2
        if nums[mid] == target {
            return mid
        // 左边有序
        } else  if nums[mid] < nums[right] {
            if nums[mid] < target && target <= nums[right] {
                left = mid + 1
            } else {
                right = mid - 1
            }
        // 右边有序
        } else {
            if nums[left] <= target && target < nums[mid] {
                right = mid - 1
            } else {
                left = mid + 1
            }
        }
    }
    return -1
}
```

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return search(nums, target)
# python 简化版本
def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - r) // 2
        if nums[mid] == target: return mid
        elif nums[l] <= target <= nums[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return -1
```

---- -
**求平方根**
```python
/*实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/binary-search/xe9cog/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
*/
func mySqrt(x int) int {
    left := 0
    right := x

    for left <= right {
        mid := left + (right - left) / 2
        if mid * mid == x {
            return mid
        } else if mid * mid > x {
            right = mid - 1
        } else {
            left = mid + 1
        }
    }
    return right
}
```

---- 
二分查找的高级模板 - 查找右
```python

def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    # Post-processing:
    # End Condition: left == right
    if left != len(nums) and nums[left] == target:
        return left
    return -1
```

