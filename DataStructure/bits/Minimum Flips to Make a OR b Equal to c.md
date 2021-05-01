1318. Minimum Flips to Make a OR b Equal to c

给你三个正整数 a、b 和 c。

你可以对 a 和 b 的二进制表示进行位翻转操作，返回能够使按位或运算   a OR b == c  成立的最小翻转次数。

「位翻转操作」是指将一个数的二进制表示任何单个位上的 1 变成 0 或者 0 变成 1 。

```python
"""
算法: 如果c 第i位上bit为1: 
        a || b 的第i位为1   = 不需要翻转
                       0   = 需要翻转1次
     如果c 第i位上bit位0:
        a || b 的第i位为0  = 不需要翻转
        a || b 的第i位为1  = 需要翻转1 或者2次
时间复杂度：O(sizeof(max(a, b, c)))
空间复杂度：O(1)
"""

def minFlips(a: int, b: int, c: int) -> int:
    ans = 0
    while a or b or c:
        a_bit = a & 1
        b_bit = b & 1
        c_bit = c & 1
        if (a_bit | b_bit) != c_bit:
            if c_bit == 1 or (a_bit & b_bit == 0):
                ans += 1
            else:
                ans += 2
        a = a >> 1
        b = b >> 1
        c = c >> 1
    return ans
```
