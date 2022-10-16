
"""
You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.

Input: nums = [3,4,2]
Output: 6
Explanation: You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.

Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: You can perform the following operations:
- Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
- Delete a 3 again to earn 3 points. nums = [3].
- Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points.

Constraints:
    1 <= nums.length <= 2 * 104
    1 <= nums[i] <= 104
"""


from typing import List
from collections import Counter
import pytest


def deleteAndEarn(nums: List[int]) -> int:
    if not nums: return 0
    max_num = max(nums)
    if max_num == 0:
        return 0
    
    dp = [0] * (max_num + 1)
    counter = Counter(nums)
    dp[1] = counter.get(1, 0)
    
    for i in range(2, max_num + 1):
        count = counter.get(i, 0)
        dp[i] = max(count * i + dp[i - 2], dp[i - 1])
    return dp[-1]


@pytest.mark.parametrize("input, expected", [([3, 4, 2], 6), ([2, 2, 3, 3, 3, 4], 9)])
def test_deleteAndEarn(input, expected):
    ans = deleteAndEarn(input)
    assert ans == expected



