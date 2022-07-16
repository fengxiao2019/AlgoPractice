
"""
值域二分
最大值为右下角的元素 min_v
最小值为左上脚的元素 max_v
第k个元素只可能出现在 min_v 和 max_v之间，假设第k个元素为f(k)

现在问题转化为计算在m n构成的表格中比f(k)小的元素的个数，假设为c(k)
if c(k) > == k - 1 && c(k)存在于表格中，那么就是结果
如果c(k) < k - 1: 增加f(k)的值
如果c(k) > k - 1: 降低f(k)的值

怎么计算c(k) 以及如何确认c(k)存在于表格中呢？

针对f(k)，对于行i，小于f(k)的元素的个数为min(f(k)//i, n) n为列的个数
"""


def lessCount(m: int, n: int, target: int):
    count = 0
    for i in range(1, m + 1):
        count += min(target//i, n)
    return count


def findKthNumber(m: int, n: int, k: int) -> int:
    l, r = 1, m * n + 1
    while l < r:
        mid = l + (r - l) // 2
        if lessCount(m, n, mid) >= k:
            r = mid
        else:
            l = mid + 1
    return l