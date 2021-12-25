20210814 - 买卖股票的最佳利润

> 给定一个数组 prices ，它的第 i 个元素 prices[i]() 表示一支给定股票第 i 天的价格。
> 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
> 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
```python
class Solution:
    """
    # 暴力解法
    时间复杂度：O(n^2)
    空间复杂度：O(1)
    """
    def maxProfit(self, prices: List[int]) -> int:
        max_v = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    continue
                max_v = max(max_v, prices[j] - prices[i])
        return max_v
    
    """
    单调栈解法
    时间复杂度：o(n)
    空间复杂度：O(n)
    """
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        max_v = 0
        for item in prices:
            if stack and stack[-1] > item:
                while stack and stack[-1] > item:
                    stack.pop()
            stack.append(item)
            if len(stack) >= 2:
                max_v = max(stack[-1] - stack[0], max_v)
        return max_v
    
    """
    dp[i] 表示i前面最小值（包括i）
    max_v = max(max_v, prices[i] - dp[i-1])
    时间复杂度：O(n)
    空间复杂度：O（n)
    """
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        dp = [sys.maxsize for _ in range(len(prices))]
        dp[0] = prices[0]
        max_v = 0
        for i in range(1, len(prices)):
            dp[i] = min(prices[i], dp[i-1])
            max_v = max(max_v, prices[i] - dp[i-1])
        return max_v 

    """
    dp[i]i前能获取的最大利润（包括i）
    相似题：最大子序列和
	时间复杂度：O(n)
	空间复杂度：O(1)
    """
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        dp = [0] * (len(prices))
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            if dp[i-1] < 0:
                dp[i] = diff
            else:
                dp[i] = dp[i-1] + diff
        return max(dp)
```

