
给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回  -1 。

```python
"""
暴力解法

固定i，匹配haystack[i: i + m], i = 0, 1, 2, ..., n - m
约束条件: 
不存在返回什么？
有可能过出现空串吗？
空串怎么处理？
时间复杂度：O(mn) n 为haystack的长度，m为needle的长度
空间复杂度：O(1)
"""
def str_str(haystack: str, needle: str) -> int:
    n, m = len(haystack), len(needle)
    for i in range(n - m + 1):
        if haystack[i: i + m] == needle:
            return i
    return -1



"""
因为在暴力解法中，有很多运算是无效，可以利用pattern中prefix的maxoverlap减少无效的运算
实际返回的是maxoverlap(prefix)
aaabaaa
dp = [0, 1, 2]
    aa     aaa     aaab          aaaba          aaabaa            aaabaaa
     aa     aaa        aaab          aaaba          aabaa             aaabaaa
i 0   1      2     0                1             2                   3
j 1   2      3     4                5             6                   7
failure_function 返回结果 = [0, 1, 2, 0, 1, 2, 3]
"""

def kmp(origin: str, pattern: str) -> int:
    i, j = 0, 0
    n, m = len(origin), len(pattern)
    if m == 0: return 0
    dp = failure_function(pattern)
    while i < n and j < m:
        if origin[i] == pattern[j] and j == m - 1:
            return i - j
        elif origin[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if j > 0:
                j = dp[j - 1]
            else:
                i += 1
    return -1

def failure_function(pattern: str) -> List[int]:
    res = [0] * len(pattern)
    i, j = 0, 1
    while j < len(pattern):

        if pattern[j] == pattern[i]:
            res[j] = i + 1
            i += 1
            j += 1
        elif i == 0:
            res[j] = 0
            j += 1
        else:
            i = res[i - 1]  # 从下一个有效匹配的段开始找合适的位置
    print(res)
    return res

```
