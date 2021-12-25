from typing import List
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        return sumSubarrayMins(arr)


"""
解题思路：递增栈
3   1   2   4
sum(min(b)) = f(i) * nums[i]  i = 0 1 2  ... n-1
f(i) 表示以nums[i]为最小值的子数组的个数

怎么确定以nums[i] 为子数组的个数？

3  1   2    4 
0  1   2    3
   ^   *       ^
对于下标为2的元素，ple（previous less number） 是1
                nle (next less number) 不存在，相当于len(nums)
ple ~ 2 的距离 dis_ple 为 2 - 1 = 1
2 ～ nle 的距离 dis_nle 为 4 - 2 = 2
2
2 4

因此2 对结果的贡献为：2 * (dis_ple * dis_nle) = 2 * (1 * 2) = 4
对于nums[i] 对结果的贡献为：nums[i] * ((i - ple) * (nle - i))
复杂度：
时间复杂度：O(n)
空间复杂度：O(n)
"""


def sumSubarrayMins(arr: List[int]) -> int:
    previous_res = previous_less_index(arr)
    next_res = next_less_index(arr)
    sum_v = 0
    for i in range(len(arr)):
        pre_dis = i - previous_res[i]
        next_dis = next_res[i] - i

        sum_v += arr[i] * (next_dis * pre_dis)
    return sum_v % (pow(10, 9) + 7)


def previous_less_index(arr: List[int]) -> List[int]:
    stack = []
    previous_res = [-1] * len(arr)
    for i in range(len(arr)):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        if stack:
            previous_res[i] = stack[-1]
        stack.append(i)
    return previous_res


def next_less_index(arr: List[int]) -> int:
    stack = []
    next_res = [len(arr)] * len(arr)
    for i in range(len(arr)):
        while stack and arr[stack[-1]] > arr[i]:
            next_res[stack[-1]] = i
            stack.pop()
        stack.append(i)
    return next_res