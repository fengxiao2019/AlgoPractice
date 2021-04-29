"""
冒泡排序算法
"""
class BubbleSort(object):
    def __call__(self, nums):
        self._helper(nums)

    def _helper(self, nums):
        i = len(nums) - 1
        while i >= 0:
            j = 1
            while j <= i:
                if nums[j - 1] > nums[j]:
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j += 1
            i -= 1