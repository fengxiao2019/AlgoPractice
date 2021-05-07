from typing import List
import heapq
"""
暴力解法 + 最大堆
时间复杂度：O(n^2logk)
空间复杂度：O(k)
"""


def smallestDistancePair(nums: List[int], k: int) -> int:
    heap = []
    heapq.heapify(heap)
    nums.sort()

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            diff = nums[j] - nums[i]
            heapq.heappush(heap, -diff)
            if len(heap) > k:
                heapq.heappop(heap)

    res = heapq.heappop(heap)
    return -res


"""
二分查找
    可以通过排序获取最小距离 和 最大距离，然后在这个范围内进行查找。
    针对每个距离，如果当前这个距离刚好是第k个，就返回这个距离
时间复杂度：O(nlogn)
空间复杂度：O(1)
"""


def smallestDistancePair(nums: List[int], k: int) -> int:
    # O(nlogn)
    nums.sort()
    # O(n)
    l = min([nums[i + 1] - nums[i] for i in range(len(nums) - 1)])
    r = nums[-1] - nums[0]
    # O(log(r-l))
    while l < r:
        mid = l + ((r - l) >> 2)
        if countPairs(nums, mid) < k:
            l = mid + 1
        else:
            r = mid
    return l


def countPairs(nums: List[int], mid: int) -> int:
    count = 0
    j = 1
    # O(n)
    for i in range(len(nums)):
        while j < len(nums) and nums[j] - nums[i] <= mid:
            j += 1
        count += j - i - 1
    return count