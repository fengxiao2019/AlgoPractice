from typing import List


class InsertSort(object):
    def __call__(self, nums: List[int]) -> None:
        self._helper(nums)

    def _helper(self, nums: List[int]) -> None:
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                j += 1
            i += 1