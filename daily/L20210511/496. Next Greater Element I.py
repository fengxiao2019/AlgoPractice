"""
先对nums2进行遍历，确认下标i的元素
"""
from typing import List


def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    stack = []
    hash_map = {}
    for i in range(len(nums2)):
        if stack and stack[-1] < nums2[i]:
            while stack and stack[-1] < nums2[i]:
                hash_map[stack[-1]] = nums2[i]
                stack.pop()

        stack.append(nums2[i])
    res = []
    print(hash_map)
    for item in nums1:
        res.append(hash_map.get(item, -1))
    return res