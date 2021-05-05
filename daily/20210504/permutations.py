#22. Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""
Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
"""
from typing import List

"""
This can be seen as a full alignment with duplicate characters, using hash table de-duplication
"""
def generate_parentheses(n: int) -> List[str]:
    # 定义返回结果
    ans = []
    # 定义hashmap
    hash_map = {'(': n, ')': n}
    def dfs(combine: str) -> None:
        if len(combine) == 2 * n:
            if valid(combine):
                ans.append(combine)
            return

        for k, v in hash_map.items():
            if v == 0: continue
            combine += k
            hash_map[k] -= 1
            dfs(combine)
            combine = combine[:-1]
            hash_map[k] += 1
    dfs("")
    return ans

"""
Optimized version
A string is invalid when the number of ')' inside the string is greater than '('
"""
def generate_parentheses(n: int) -> List[str]:
    # 定义返回结果
    ans = []
    # 定义hashmap
    hash_map = {'(': n, ')': n}
    def dfs(combine: str) -> None:
        if len(combine) == 2 * n:
            ans.append(combine)
            return

        for k, v in hash_map.items():
            if v == 0 or hash_map['('] > hash_map[')']: continue
            combine += k
            hash_map[k] -= 1
            dfs(combine)
            combine = combine[:-1]
            hash_map[k] += 1
    dfs("")
    return ans


# verify the combine is valid
def valid(combine: str) -> bool:
    balance = 0
    hash_map = {'(': 1, ')': -1}
    for item in combine:
        if balance < 0: return False
        balance += hash_map[item]
    return balance == 0


"""
全排列
https://leetcode-cn.com/problems/permutations/
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""


def permutations(nums: List[int]) -> List[List[int]]:
    ans = []
    visited = {}
    def dfs(combine: List[int]) -> None:
        if len(combine) == len(nums):
            ans.append(combine[:])
            return
        for i in range(0, len(nums)):
            if visited.get(i, False):
                continue

            combine.append(nums[i])
            visited[i] = True
            dfs(combine)
            combine.pop()
            visited[i] = False
    dfs([])
    return ans
"""
解法2：原地交换
"""
def permutations(nums: List[int]) -> List[List[int]]:
    ans = []
    def dfs(index: int) -> None:
        if index == len(nums):
            ans.append(nums[:])
            return
        for i in range(index, len(nums)):
            nums[i], nums[index] = nums[index], nums[i]
            dfs(index + 1)
            nums[i], nums[index] = nums[index], nums[i]
    dfs(0)
    return ans
"""
31. Next Permutation
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

"""
"""
step1: 从右向左找到第一个a[i - 1] < a[i]的i
step2: 在a[i:]中从右->左 找到第一个大于a[i-1]的a[j], 前提是i > 0
step3: swap a[i - 1], a[j]
step4: 翻转 a[i:]
"""
def next_permutation(nums: List[int]) -> List[int]:
    i = len(nums) - 1
    while i > 0:
        if nums[i-1] < nums[i]:
            break
        i -= 1
    # step2:
    j = len(nums) - 1
    if i > 0:
        while j >= i:
            if nums[j] > nums[i-1]:
                break
            j -= 1
    nums[i - 1], nums[j] = nums[j], nums[i - 1]
    nums[:] = nums[:i] + nums[i:][::-1]


# def permutations(nums: List[int]) -> List[List[int]]:
#     pass

"""
全排列，有重复元素
"""