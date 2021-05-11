"""
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.
"""

"""
hash 表存储key: sum, val: [(1,1)] 
时间复杂度：O((m*n+k)log(k))
空间复杂度：O(m*n) + O(k)
"""

from typing import List
from collections import defaultdict
import heapq

def kSmallestPairs(nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    hash_table = defaultdict(list)

    heap = []
    heapq.heapify(heap)
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            sum_v = nums1[i] + nums2[j]
            if sum_v not in hash_table:
                heapq.heappush(heap, -sum_v)
            if len(heap) > k:
                heapq.heappop(heap)
            hash_table[sum_v].append([nums1[i], nums2[j]])

    res = []
    heap.sort(key=lambda x: -x)
    count = 0

    for item in heap:
        for pair in hash_table[-item]:
            res.append(pair)
            count += 1
            if count == k:
                return res
    return res


"""
时间复杂度：O((m*n)log(k))
空间复杂度：O(k)
"""


def kSmallestPairs(nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    heap = []
    heapq.heapify(heap)
    for n1 in nums1:
        for n2 in nums2:
            heapq.heappush(heap, (-(n1 + n2), [n1, n2]))
            if len(heap) > k:
                heapq.heappop(heap)
    return [item[1] for item in heap]