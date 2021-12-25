from typing import List
class Solution:
    """
    以leetcode为例，dp[i] 表示前i个字符是否可以被空格拆分成一个或多个在字典中出现的单次。
    那么dp[j] = dp[i] 并且 s[i:j]
    dp[0] = True
    时间复杂度：O(n^n)
    空间复杂度：O(n)
    """

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s: return False
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(0, len(s)):
            for j in range(i + 1, len(s) + 1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[-1]

