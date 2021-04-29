import heapq


class HeapSort(object):
    def __call__(self, nums):
        self._helper(nums)

    def _helper(self, nums):
        heapq.heapify(nums)
        for i in range(len(nums)):
            nums[i] = heapq.heappop(nums[i:])