"""
冒泡排序算法
"""
class BubbleSort(object):
    def __call__(self, nums):
        self._helper(nums)
    def _helper(self, nums):
        for i in range(len(nums) - 1, -1, -1):
            for j in range(1, i+1):
                if nums[j - 1] > nums[j]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]