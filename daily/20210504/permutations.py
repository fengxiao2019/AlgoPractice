#22. Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""
Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
"""
from typing import List

"""
这个可以看成有重复字符的全排列, 利用hash表去重
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

# verify the combine is valid
def valid(combine: str) -> bool:
    balance = 0
    hash_map = {'(': 1, ')': -1}
    for item in combine:
        if balance < 0: return False
        balance += hash_map[item]
    return balance == 0
