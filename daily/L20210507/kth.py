"""
寻找两个有序数组的第k个元素
"""
from typing import List

"""
寻找两个有序数组的第k个元素
"""


def kth(nums1: List[int], nums2: List[int], k: int) -> int:
    # 处理边界条件
    if not nums1: return nums2[k]
    if not nums2: return nums1[k]

    mid_1 = len(nums1) // 2
    mid_2 = len(nums2) // 2
    v_1 = nums1[mid_1]
    v_2 = nums2[mid_2]

    if mid_1 + mid_2 < k:
        if v_1 > v_2:
            return kth(nums1, nums2[mid_2+1:], k - mid_2 - 1)
        else:
            return kth(nums1[mid_1+1:], nums2, k - mid_1 - 1)
    else:
        if v_1 > v_2:
            return kth(nums1[:mid_1], nums2, k)
        else:
            return kth(nums1, nums2[:mid_2], k)


import unittest


class TestKth(unittest.TestCase):
    def test_kth(self):
        self.assertEqual(kth([1, 4, 7, 9], [2, 6, 10], 1), 2)