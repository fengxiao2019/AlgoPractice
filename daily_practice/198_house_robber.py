"""
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from
robbing each of them is that
adjacent houses have security systems connected
and it will automatically contact the police
if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.
"""
from typing import List
import pytest


def rob(nums: List[int]) -> int:
    # calculate the length of the arr
    length = len(nums)
    if length == 0: return 0
    if length <= 2: return max(nums)
    # define the dp arr
    dp = [0] * length
    dp[0], dp[1] = nums[0], max(nums[0],nums[1])
    for i in range(2, length):
        dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
    return dp[-1]


@pytest.mark.parametrize("input, expected", 
        [([1, 2, 3], 4),
         ([1, 3, 4], 5),
         ([3, 4], 4)]
        )

def test_rob(input, expected):
    ans = rob(input)
    assert ans == expected

