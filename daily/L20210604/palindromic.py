"""
回文相关的题目
"""

"""
检查是否是回文串
680.
常用解法：双指针， 动态规划
类似的：
检查一个数是否是回文数
回文链表
求最长回文串
"""

# 647. 回文子串
# 解题思路是动态规划
# 5. 最长回文子串的解题思路一致
class Solution:
    """
    if s[i] == s[j]:
        dp[i][j] = dp[i-1][j-1]
    如果 s的长度为1: 返回 1

    时间复杂度：O(n^2)
    空间复杂度：O(n^2)
    """
    def countSubstrings(self, s: str) -> int:
        if len(s) <= 1: return len(s)

        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True

        count = len(s)
        for l in range(2, len(s) + 1):
            for i in range(len(s)):
                # l = j - i + 1
                j = l + i - 1
                if j >= len(s):
                    continue
                if s[i] == s[j]:
                    if l == 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j]:
                    count += 1
        return count

# 找最长回文串
"""
给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
注意:
假设字符串的长度不会超过 1010。
"""
import collections
class Solution:
    """
    先统计每个字符出现的次数，a = 1 b = 2
    字符出现的次数 x
    如果 x % 2 == 1:
        count += x - 1
    else:
        count += x
    如果s的长度为偶数：
       s的长度为奇树：count += 1
    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    def longestPalindrome(self, s: str) -> int:
        char_counter = collections.Counter(s)
        ans = 0
        for _, count in char_counter.items():
            if count % 2 == 1:
                ans += count - 1
            else:
                ans += count

        if len(s) == ans:
            return ans
        else:
            return ans + 1

"""
检查是否可以通过排列组合成回文串
"""

"""
检查一个
"""