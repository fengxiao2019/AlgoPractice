# basic operation
# a = 0^a or a^0
# 0 = a^a
# exchange
# a = a^b
# b = a^b
# a = a^b
# proof: 
# b = a^b^b # put a to b, because a == a^b^b, so b = a^b^b is a
# because we first put a = a^b, so b = a^b
# a = a^b=> (a^b)^(a^b^b)=> (a^b^a^b^b) => b

# remove the last 1 of n
# a=n&(n-1)
# get the last 1 of n
# diff=(n&(n-1))^n

# question1 : 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素
# 利用异或原理 a ^ a = 0 and a ^ 0 = a，可以找到只出现了一次的元素
# %%

def singleNumber(numbers: []) -> int:
    number = 0
    for item in numbers:
        number = number ^ item
    return number


numbers = [1, 1, 4]
print(singleNumber(numbers))

# %%
"""
# 给定一个非空整数数组，除了某个元素只出现一次以外，
# 其余每个元素均出现了三次。
# 找出那个只出现了一次的元素。
"""
def singleNumberII(numbers: []) -> int:
    result = 0
    for i in range(65):
        sum_v = 0
        for item in numbers:
            sum_v += (item >> i) & 1
        result += (sum_v % 3) << i
    return result

numbers = [129, 12, 129, 129]
print(singleNumberII(numbers))


# %%

"""
给定一个整数数组 nums，
其中恰好有两个元素只出现一次，
其余所有元素均出现两次。 
找出只出现一次的那两个元素。
"""

def singleNumberIII(numbers: []):
    """
    a = a ^ b
    b = a ^ b
    a = a ^ b
    """
    diff = 0
    for item in numbers:
        diff ^= item
    results = [diff, diff]
    diff = (diff & (diff - 1)) ^ diff
    for item in numbers:
        if item & diff == 0:
            results[0] = results[0] ^ item
        else:
            results[1] = results[1] ^ item
    return results


numbers = [12, 12, 14, 14, 15, 16]
print(singleNumberIII(numbers))
# %%
# 编写一个函数，
# 输入是一个无符号整数，
# 返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。


def hanming(number):
    count = 0
    while number != 0:
        count += number & 1
        number = number >> 1
    return count


def hanming_2(number):
    count = 0
    while number:
        number = number & (number - 1)
        count += 1
    return count


number = 23
print(bin(number), hanming(number), hanming_2(number))
        
# %%

# 给定一个非负整数 num。
# 对于 0 ≤ i ≤ num 范围中的每个数字 i，
# 计算其二进制数中的 1 的数目并将它们作为数组返回。
# 解法：动态规划
def count_1s(num):
    res = [0 for i in range(num + 1)]
    for i in range(1, num + 1):
        # 上一个缺1的元素 + 1
        res[i] = res[i & (i - 1)] + 1
    return res


print(count_1s(29))

# %%
# 颠倒给定的 32 位无符号整数的二进制位。
def reverse_number(num):
    res = 0
    pow_number = 31
    while num:
        res += (num & 1) << pow_number
        num = num >> 1
        pow_number -= 1
        
    return res

res = reverse_number(43)
print(f"{bin(43)},  {res},  {bin(res)}")
# %%

# 给定范围 [m, n]，其中 0 <= m <= n <= 2147483647，
# 返回此范围内所有数字的按位与（包含 m, n 两端点）。
## 按位与的操作，遇0为0
## 如果所有位都为1，那么所有值都相等
## 基于以上两点，做完位运算，所有的值应该都相等了

def range_bitwise_and(m, n):
    v = n
    for i in range(m, n):
        v &= i
    return v

def range_bitwise_and_I(m, n):
    count = 0
    while m != n:
        m >>= 1
        n >>= 1
        count += 1
    return m << count


print(range_bitwise_and(187, 188), range_bitwise_and_I(187, 188))