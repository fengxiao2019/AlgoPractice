"""
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Returns the element representing the kth largest element in the stream.

Example 1:

Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

"""
from typing import List
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        heapq.heapify(self.heap)
        self.capacity = k
        for item in nums:
            heapq.heappush(self.heap, item)
            if len(self.heap) > k:
                heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.capacity:
            heapq.heappop(self.heap)
        # v = heapq.heappop(self.heap)
        # heapq.heappush(self.heap, v)
        return self.heap[0]
