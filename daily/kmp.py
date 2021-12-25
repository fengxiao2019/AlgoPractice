"""
pattern matching
"""
from typing import List
import unittest


"""
时间复杂度：O(m+n)
空间复杂度：O(m)
"""
def kmp(origin: str, pattern: str) -> int:
    i, j = 0, 0
    n, m = len(origin), len(pattern)
    dp = failure_function(pattern)
    while i < n and j < m:
        if origin[i] == origin[j] and j == m - 1:
            return i - j
        elif origin[i] == origin[j]:
            i += 1
            j += 1
        else:
            j = dp[j - 1]
            if j == 0:
                i += 1
    return -1



"""
实际返回的是maxoverlap(prefix)
aaabaaa
dp = [0, 1, 2]
    aa     aaa     aaab          aaaba          aaabaa            aaabaaa
     aa     aaa        aaab          aaaba          aabaa             aaabaaa
i 0   1      2     0                1             2                   3
j 1   2      3     4                5             6                   7

"""
def failure_function(pattern: str) -> List[int]:
    m = len(pattern)
    res = [0] * m
    i, j = 0, 1

    while j < m:
        if pattern[i] == pattern[j]:
            res[j] = i
            i += 1
            j += 1
        elif i == 0:
            res[j] = 0
            j += 1
        else:
            i = res[i - 1]
    return res

"""
test cases
"""
class KMPTestCase(unittest.TestCase):
    pass


