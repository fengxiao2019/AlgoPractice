"""
Given an array arr[] of size n containing integers. The problem is to find the length of the longest sub-array having sum equal to the given value k.
Examples:


Input : arr[] = { 10, 5, 2, 7, 1, 9 },
            k = 15
Output : 4
The sub-array is {5, 2, 7, 1}.

Input : arr[] = {-5, 8, -14, 2, 4, 12},
            k = -5
Output : 5
"""

from typing import List
def lenOfLongSubarr(arr: List[int], k: int):
    # 最长子序列求和  # 相关问题 1124. 表现良好的最长时间段
    # 解决思路前缀和
    # hash_map 存储已经前缀和，key: sum_v   value: index
    hash_map = {}
    sum_v = 0
    max_len = 0
    n = len(arr)
    for i in range(n):
        sum_v += arr[i]
        if sum_v == k:
            max_len = i + 1
        elif sum_v - k in hash_map:
            max_len = max(max_len, i - hash_map[sum_v - k])

        hash_map.setdefault(sum_v, i)
    return max_len

if __name__ == '__main__':
    arr = [10, 5, 2, 7, 1, 9]
    k = 15

    assert(lenOfLongSubarr(arr, k) == 4)
    print(1)
