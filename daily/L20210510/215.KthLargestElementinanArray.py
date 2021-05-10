from typing import List
import heapq
"""
解题思路：
按照从大到小的顺序排序，然后取第k个元素
Time complexity: O(nlogn)
Space complexity: O(1)
"""


def findKthLargest(nums: List[int], k: int) -> int:
    if k > len(nums) or k <= 0: return None
    nums.sort(reverse=True)
    return nums[k - 1]


"""
解题思路：
维护一个数量为k的最大堆，遍历完所有的数据之后，弹出第堆的第k个元素，就是第k大元素
Time Complexity: O(n)
Space Complexity: O(k)
"""


def findKthLargest(nums: List[int], k: int) -> int:
    heap = []
    heapq.heapify(heap)
    for item in nums:
        heapq.heappush(heap, item)
        if len(heap) > k:
            heapq.heappop(heap)
    return heapq.heappop(heap)


"""
解题思路：用快速选择算法
因为是找到第k大的元素，所以，只需要找到下标为m的元素，m必须要满足以下条件：
1. m左边的元素都小于nums[m],m右边的元素都大于等于nums[m]
2. m右边的元素的个数为k - 1，也就是m + k - 1 = len(nums) - 1, m = len(nums) - k
时间复杂度：O(n)
空间复杂度：(log(n))
"""


def findKthLargest(nums: List[int], k: int) -> int:
    ans = 0

    def partion(lt: int, rt: int) -> int:
        pivot = nums[rt]
        i = lt
        for j in range(lt, rt):
            # 把比pivot小的元素都移动到左边
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        # 将rt移动到i的位置
        nums[i], nums[rt] = nums[rt], nums[i]
        return i

    # 递归写法
    def findKthLargestHelper(lt: int, rt: int):
        nonlocal ans
        # print(lt, rt)
        if lt <= rt:
            index = partion(lt, rt)
            # print(nums)
            if index == len(nums) - k:
                ans = nums[index]
                return
            elif index > len(nums) - k:
                findKthLargestHelper(lt, index - 1)
            else:
                findKthLargestHelper(index + 1, rt)

    # 非递归写法
    def findKthLargestHelper(lt: int, rt: int):
        nonlocal ans
        while True:
            index = partion(lt, rt)
            if index == len(nums) - k:
                ans = nums[index]
                return
            elif index > len(nums) - k:
                rt = index - 1
            else:
                lt = index + 1

    findKthLargestHelper(0, len(nums) - 1)
    return ans