338. Counting Bits
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
示例 1:
```python
输入: 2
输出: [0,1,1]
```
示例 2:
```python
输入: 5
输出: [0,1,1,2,1,2]
```

```python
"""
逐个计算每个元素中1的个数
时间复杂度：O(n*sizeof(n))
空间复杂度：O(n)
"""

def countBits(num: int) -> List[int]:
    # 定义返回结果
    ans = []
    for i in range(num + 1):
        ans.append(countBitsOfInteger(i))
    return ans


def countBitsOfInteger(num: int):
    count = 0
    while num:
        if num & 1: count += 1
        num = num >> 1
    return count

    """
    优化的解法：假设n 中二进制位上为1的个数 为f(n)
    f(n) = f(n& (n-1)) + 1
    用一个长度为n+1的数组counts保存f(n)的结果
    count[n] 就是最后的结果
    时间复杂度:O(n)
    空间复杂度：O(n)
    """

    def countBits(num: int) -> List[int]:
        dp = [0] * (num + 1)
        for i in range(1, num + 1):
            dp[i] = dp[i & (i - 1)] + 1
        return dp[num]
```
