"""
单调递增栈
"""
from typing import List
def findNextGreater(nums: List[int]) -> List[int]:
    stack = []
    ans = [-1] * len(nums)
    for i, v in enumerate(nums):
        while stack and nums[stack[-1]] < v:
            top_i = stack.pop()
            ans[top_i] = v
        stack.append(i)
    return ans

"""
单调递减栈
"""
def findNextSmaller(nums: List[int]) -> List[int]:
    stack = []
    ans = [-1] * len(nums)
    for i, v in enumerate(nums):
        while stack and nums[stack[-1]] > v:
            top_i = stack.pop()
            ans[top_i] = v
        stack.append(i)
    return ans


def findPreviousGreater(nums: List[int]) -> List[int]:
    stack = []
    ans = [-1] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        v = nums[i]
        while stack and nums[stack[-1]] < v:
            top_i = stack.pop()
            ans[top_i] = v
        stack.append(i)
    return ans


def findPreviousSmaller(nums: List[int]) -> List[int]:
    stack = []
    ans = [-1] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        v = nums[i]
        while stack and nums[stack[-1]] > v:
            top_i = stack.pop()
            ans[top_i] = v
        stack.append(i)
    return ans


import  unittest

class BaseTestMonoStack(unittest.TestCase):
    def setUp(self) -> None:
        self.empty = []
        self.one = [4]
        self.two = [4, 5]
        self.multi = [4, 5, 3, 1]

    def test_empty(self):
        self.assertEqual(findNextGreater([]), [])

    def test_one(self):
        self.assertEqual(findNextGreater([4]), [-1])


class TestMonoIncreaseStack(BaseTestMonoStack):

    def test_two(self):
        self.assertEqual(findNextGreater([4,5]), [5, -1])


class TestMonoIncreaseStackBackward(BaseTestMonoStack):
    def test_two(self):
        self.assertEqual(findPreviousGreater([4,5]), [-1, -1])

    def test_multi(self):
        self.assertEqual(findPreviousGreater([4, 5, 3, 1]), [-1, -1, 5, 3])


class TestMonodecreaseStack(BaseTestMonoStack):
    def test_two(self):
        self.assertEqual(findPreviousGreater([4, 5]), [-1, -1])

    def test_multi(self):
        self.assertEqual(findNextSmaller([4, 5, 3, 1]), [3, 3, 1, -1])


class TestMonodecreaseStackBackward(BaseTestMonoStack):
    def test_two(self):
        self.assertEqual(findPreviousSmaller([4, 5]), [-1, 4])

    def test_multi(self):
        self.assertEqual(findPreviousSmaller([4, 5, 3, 1]), [-1, 4, -1, -1])
