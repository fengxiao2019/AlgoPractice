# 81. 搜索旋转排序数组II
# 解题方法：二分查找
#    旋转后的数组存在的特性：从任意索引切成两个数组，其中必然有一个数组是有序的
#
#    如果target在有序数组内，使用二分查找查询
#    如果target不在有序数组内，另外一半数组仍然是一个满足旋转过的数组
#    还可以继续进行搜索旋转数组的逻辑

#  问题：
#    如何判断哪个数组有序？
#      无重复元素
#        假设切分处的索引为mid，nums 开始的索引为start，结束的索引为end
#        如果 nums[start] <= nums[mid]，说明[start, mid]都是有序的
#        否则，就是[mid, end]是有序的
#
#      存在重复元素的情况下?
#        在有重复元素的情况下，会出现一种特殊情况
#        nums[start] == nums[mid] == nums[end]
#        缩小数组 start += 1 end -= 1, 重新搜索

# 边界条件处理：
# 出现bug的地方：
# 1. 如何判断一个数组是否是有序数组？
#    是 nums[start] < nums[mid]   记为A 语句
#    还是nums[start] <= nums[mid]?  记为B 语句
#    eg: [1, 0]  start = 0, mid = 0, end = 1, target = 1
#    这种场景下，如果是A语句的话，会找不到target，所以，需要选择B语句这种写法
# 81. 搜索旋转排序数组II
# 时间复杂度：O(n) 在代码38-40行，如果数组内的所有元素都相等
# 并且不等于target，那么需要n/2次迭代，也就是O(n/2)，即O(n)
# 其他情况下，时间复杂度等于二分查找的时间复杂度O(logn)
# 大O表示法表示的是最糟糕的场景，所以该算法的时间复杂度为O(n)

# 空间复杂度：O(1) 迭代，没有递归产生的栈空间，定义的是常量个变量，所以复杂度为O(1)
#
from typing import List


def search(nums: List[int], start: int, end: int, target: int) -> bool:
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return True
        if nums[start] == nums[mid] == nums[end]:
            start += 1
            end -= 1
        # [start, mid] 为有序区间
        elif nums[start] <= nums[mid]:
            if nums[start] <= target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if nums[mid] < target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1
    return False


# 采用递归的方式求解
def search_recursion(nums: List[int], start: int, end: int, target: int) -> bool:
    # 怎么退出
    if start > end:
        return False

    mid = (start + end) // 2
    if nums[mid] == target:
        return True
    elif nums[start] == nums[mid] and nums[mid] == nums[end]:
        start += 1
        end -= 1
        return search(nums, start, end, target)
    # 判断 start - end 是否满足有序序列
    elif nums[start] <= nums[mid]:
        # 如果target在有序数组内
        if nums[start] <= target < nums[mid]:
            return binary_search(nums, start, mid - 1, target)
        else:
            return search(nums, mid + 1, end, target)
    else:
        if nums[mid] < target <= nums[end]:
            return binary_search(nums, mid + 1, end, target)
        else:
            return search(nums, start, mid - 1, target)


## binary_search
# 二分查找，end 是选择数组的长度还是选择数组长度-1？
# eg, nums = [1, 3, 5, 7, 9]
#     start    mid     end        target = 10
#       0       2       5
#       3       4       5
#       5       5       5
# mid的值为5了，这个时候，就会出现index out of range
# 所以，end 的值最大只能为len(nums) - 1

# 二分查找
def binary_search(nums, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return True
        elif target > nums[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return False
