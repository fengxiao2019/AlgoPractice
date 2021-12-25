"""
枚举
因为是前n个正整数，所以可选值的范围是确定的
假设perm数据为
[x1, x2, x3, x4, x5]
perm[0] = x1^x2^x2^x3^x3^x4^x4^x5^x5 = (x1^x2^x3^x4^x5) ^ (x2^x3^x4^x5)
        n内所有元素xor ^ encoded[1:] step = 2 范围内元素的xor
找到perm[0],就可以逐个求出perm中的元素了。
perm[1] = perm[0] xor (encoded[0])
perm[2] = perm[1] xor(encoded[1])
perm[n-1] = perm[n-2] xor (encoded[n-2])
时间复杂度：O(n)
空间复杂度：O(n)
"""
from typing import List


def decode(encoded: List[int]) -> List[int]:
    total = 0
    for i in range(1, len(encoded) + 2):
        total ^= i
    post = 0
    for i in range(1, len(encoded), 2):
        post ^= encoded[i]

    perm = [total ^ post]
    for i in range(len(encoded)):
        perm.append(perm[i] ^ encoded[i])
    return perm