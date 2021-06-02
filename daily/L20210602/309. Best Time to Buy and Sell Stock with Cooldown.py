from typing import List
class Solution:
    """
    第i天，你所处的状态有三种：
        0. 手上有股票股票
        1. 手上没有股票，处于冷冻期
        2. 手上没有股票，不处于冷冻期

    针对第一种情况，转入的场景有两个：
        1. 第i-1天手上有股票，今天不买入也不卖出
        2. 第i-1天处于“手上没有股票，不处于冷冻期”的状态，今天可以买入股票
        状态方程：f(i,1) = max(f(i-1, 0), f(i-1, 2) - prices(i))

    针对第二种情况，转入的场景有一个
        1. 第i天结束时卖出了股票，那就要求第i-1天手上必须有股票
        f(i, 1) = f(i-1, 0) + prices[i]

    针对第三种情况：
        1. 第i-1天 “手上没有股票，不处于冷冻期”，第i天也不卖入
        2. 第i-1天 “手上没有股票，处于冷冻期” 今天刚好解冻
        f(i,2) = max(f(i-1, 1), f(i-1, 2))
    最后的结果：max(f(n-1, 1), f(n-2, 2))

    边界：
    f(0, 0) = -prices[0]
    f(0, 1) = 0
    f(0, 2) = 0

    时间复杂度：O(n)
    空间复杂度：O(n)
    """

    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        max_profit = [[0, 0, 0] for _ in range(len(prices))]
        max_profit[0][0] = -prices[0]
        for i in range(1, len(prices)):
            # f(i,1) = max(f(i-1, 0), f(i-1, 2) - prices(i))
            max_profit[i][0] = max(max_profit[i - 1][0], max_profit[i - 1][2] - prices[i])
            max_profit[i][1] = max_profit[i - 1][0] + prices[i]
            max_profit[i][2] = max(max_profit[i - 1][1], max_profit[i - 1][2])
        return max(max_profit[len(prices) - 1][1], max_profit[len(prices) - 1][2])




