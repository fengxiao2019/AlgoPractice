"""
初始的丑数是1
下一个数就所有已经计算的丑数 * (2, 3, 5)中最小值
因为越靠前的数与2， 3， 5想乘得到的结果也越小。
我们可以维持三个指针，分别为M2 M3 M5 ，在每次计算时，下一个丑数 ugv = min(M2 * 2, M3 * 3, M5 * 5)
计算完之后，更新M2 M3 M5的值，确保下一个丑数大于ugv
时间复杂度：O(n)
空间复杂度：O(n)
"""


class Solution(object):
    def GetUglyNumber(self, n: int):
        """
        给你一个整数n，请你找出并返回第n个丑数
        丑数是只包含质因数 2  3  5 的正整数
        https://leetcode-cn.com/problems/ugly-number-ii/
        """
        if n <= 0: return 0
        uglyNUmbers = [0] * n
        uglyNUmbers[0] = 1
        m2, m3, m5 = 0, 0, 0
        for i in range(1, n):
            min_v = min(uglyNUmbers[m2] * 2, uglyNUmbers[m3] * 3, uglyNUmbers[m5] * 5)
            uglyNUmbers[i] = min_v
            while m2 < n and uglyNUmbers[m2] * 2 <= min_v:
                m2 += 1
            while m3 < n and uglyNUmbers[m3] * 3 <= min_v:
                m3 += 1
            while m5 < n and uglyNUmbers[m5] * 5 <= min_v:
                m5 += 1
        return uglyNUmbers[-1]

    def isUgly(self, n: int) -> bool:
        """
        判断一个数是否是丑数
        必须得能被2 3 5 中至少一个整除
        https://leetcode-cn.com/problems/ugly-number/
        """
        if n <= 0:
            return False
        while n > 1:
            if n % 2 == 0:
                n %= 2
            elif n % 3 == 0:
                n %= 3
            elif n % 5 == 0:
                n %= 5
            else:
                return False
        return True

    # def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
    #     if n < 0: return 0
    #     if 1 in (a, b, c): return n
    #
    #     uglyNUmbers = [0] * (n + 1)
    #     uglyNUmbers[0] = 1
    #     ma, mb, mc = 0, 0, 0
    #     for i in range(1, n + 1):
    #         min_v = min(uglyNUmbers[ma] * a, uglyNUmbers[mb] * b, uglyNUmbers[mc] * c)
    #         print(min_v, ma)
    #         uglyNUmbers[i] = min_v
    #
    #         # 过滤掉不可能成为下一个最小丑数的值,通过更新下标实现
    #         while uglyNUmbers[ma] * a <= min_v:
    #             ma += 1
    #         while uglyNUmbers[mb] * b <= min_v:
    #             mb += 1
    #         while uglyNUmbers[mc] * c <= min_v:
    #             mc += 1
    #     return uglyNUmbers[-1]


if __name__ == '__main__':

    print(Solution().nthUglyNumber(5, 2, 11, 13))