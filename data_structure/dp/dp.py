# %%
# find the rules
# the base case
# recursive algorithm
# translate recursive to dp

# coin change problem

# 直观的思路解法
def coin_change_pre(amount: int, v1: int, v2: int, v3: int) -> int:
    # base case
    if amount <= 0:
        return 0
    
    # main logic
    res = []
    if amount >= v1:
        tmp = coin_change_pre(amount - v1, v1, v2, v3)
        mysol1 = tmp + 1
        res.append(mysol1)
    
    if amount >= v2:
        tmp = coin_change_pre(amount - v2, v1, v2, v3)
        mysol2 = tmp + 1
        res.append(mysol2)
    
    if amount >= v3:
        tmp = coin_change_pre(amount - v3, v1, v2, v3)
        mysol3 = tmp + 1
        res.append(mysol3)
    
    if res:
        return min(res)
    return -1


# 改进
def coin_change(amount: int, coins: list) -> int:
    if amount <= 0:
        return 0
    sols = []

    for index, item in enumerate(coins):
        if amount >= item:
            sol = coin_change(amount - item, coins)
            sols.append(sol + 1)
    if sols:
        return min(sols)
    else:
        return 0


# 动态规划解法
# 前面的解法当amount的值大于100时就非常慢了，实际并不实用
def dp_coin_change(amount: int, coins: list) -> int:
    # store memory
    dp_array = [-1 for i in range(amount + 1)]
    # base case
    dp_array[0] = 0
    for tmp_amount in range(1, amount + 1, 1):
        sols = []
        for index, coin in enumerate(coins):
            if tmp_amount >= coin:
                tmp = dp_array[tmp_amount - coin]
                sols.append(tmp + 1)
        # calc dp_array
        dp_array[tmp_amount] = min(sols) if sols else 0

    return dp_array[amount]


def test_coin_change():
    amount = 30 
    coins = [1, 3, 5]
    res = coin_change(amount, coins)
    print(res)
    res1 = coin_change_pre(amount, 1, 3, 5)
    print(res1)

    res3 = dp_coin_change(amount, coins)
    print(res3)


test_coin_change()

# %%

# %%

# minimum edit distance


def min_distance(src: str, dst: str) -> int:
    if len(src) == 0:
        return len(dst)
    if len(dst) == 0:
        return len(src)

    if src[-1] == dst[-1]:
        mysol = min_distance(src[:-1], dst[:-1])
        return mysol
    else:
        # del
        mysol1 = min_distance(src[:-1], dst)
        # insert
        mysol2 = min_distance(src, dst[:-1])
        # replace
        mysol3 = min_distance(src[:-1], dst[:-1])
        return min(mysol1 + 1, mysol2 + 1, mysol3 + 1)


def dp_min_distance(src: str, dst: str) -> int:
    src_len = len(src)
    dst_len = len(dst)

    dp_array = [[0 for i in range(dst_len + 1)] for item in range(src_len + 1)]
    # dp_array[0][j] = j
    # dp_array[i][0] = i
    for i in range(src_len + 1):
        dp_array[i][0] = i

    for j in range(dst_len + 1):
        dp_array[0][j] = j
    for i in range(1, src_len + 1):
        for j in range(1, dst_len + 1):

            if src[i - 1] == dst[j - 1]:
                dp_array[i][j] = dp_array[i - 1][j - 1]
            else:
                dp_array[i][j] = min(dp_array[i - 1][j] + 1,  # delete
                                     dp_array[i - 1][j - 1] + 1,  # replace
                                     dp_array[i][j - 1] + 1)  # insert
    return dp_array[src_len][dst_len]


def test_min_distance():
    src = "shaoyzz"
    dst = "shaomdffd"
    res = min_distance(src, dst)
    res2 = dp_min_distance(src, dst)
    print(res, res2)


test_min_distance()
# %%


# longest subsequence
def longest_seq(str1: str, str2: str) -> int:
    # base case
    if len(str1) == 0 or len(str2) == 0:
        return 0
    
    # rules
    if str1[-1] == str2[-1]:
        tmp_res = longest_seq(str1[:-1], str2[:-1])
        return tmp_res + 1
    else:
        res1 = longest_seq(str1[:-1], str2)
        res2 = longest_seq(str1, str2[:-1])
        return max(res1, res2)


def longest_seq_str(str1: str, str2: str) -> str:
    if len(str1) == 0 or len(str2) == 0:
        return ""
    
    if str1[-1] == str2[-1]:
        tmp_res = longest_seq_str(str1[:-1], str2[:-1]) + str1[-1]
        print(f"---- {tmp_res}")
        return tmp_res
    else:
        res1 = longest_seq_str(str1[:-1], str2)
        res2 = longest_seq_str(str1, str2[:-1])
        if len(res1) > len(res2):
            return res1
        return res2


def dp_longest_seq(str1: str, str2: str) -> int:
    str1_len = len(str1)
    str2_len = len(str2)
    dp_array = [[0 for j in range(str2_len + 1)] for i in range(str1_len + 1)]
    # for i in range(str1_len + 1):
    #     dp_array[i][0] = 0
    
    # for i in range(str2_len + 1):
    #     dp_array[0][i] = 0
    
    for i in range(1, str1_len + 1):
        for j in range(1, str2_len + 1):
            if str1[i - 1] == str2[j - 1]:
                dp_array[i][j] = dp_array[i - 1][j - 1] + 1
            else:
                dp_array[i][j] = max(dp_array[i - 1][j], dp_array[i][j - 1])
    print(dp_array)
    return dp_array[str1_len][str2_len]


# 节省内存
def dp_2(str1: str, str2: str) -> int:
    str1_len = len(str1)
    str2_len = len(str2)
    dp_array = [[0 for j in range(str2_len + 1)] for i in range(2)]

    for i in range(1, str1_len + 1):
        dp_array[1][0] = 0
        for j in range(1, str2_len + 1):
            if str1[i - 1] == str2[j - 1]:
                print(str1[i - 1])
                dp_array[1][j] = dp_array[0][j - 1] + 1
            else:
                dp_array[1][j] = max(dp_array[0][j], dp_array[1][j - 1])
        print(dp_array)
        # cp dp_array[1] -> dp_array[0]
        dp_array[0] = dp_array[1]
    print(dp_array)
    return dp_array[1][str2_len]


def test_le():
    str1 = "ABCABCABC"
    str2 = "BABACBAB"
    res = longest_seq(str1, str2)
    print(res)
    res2 = dp_longest_seq(str1, str2)
    print(res2)
    res3 = dp_2(str1, str2)
    print(res3)
    str_v = longest_seq_str(str1, str2)
    print(str_v)


test_le()

# %%


def longest_substring(str1: str, str2: str) -> int:
    str1_len = len(str1)
    str2_len = len(str2)

    # base case
    if str1_len == 0 or str2_len == 0:
        return 0

    # rules
    if str1[-1] == str2[-1]:
        res = longest_substring(str1[:-1], str2[:-1]) + 1
        return res
    else:
        res1 = longest_substring(str1[:-1], str2)
        res2 = longest_substring(str1, str2[:-1])
        if res1 > res2:
            return res1
        else:
            return res2


def longest_substr(str1: str, str2: str) -> str:
    str1_len = len(str1)
    str2_len = len(str2)

    # base case
    if str1_len == 0 or str2_len == 0:
        return ""

    # rules
    if str1[-1] == str2[-1]:
        res = longest_substr(str1[:-1], str2[:-1]) + str1[-1]
        return res
    else:
        res1 = longest_substr(str1[:-1], str2)
        res2 = longest_substr(str1, str2[:-1])
        if len(res1) > len(res2):
            return res1
        else:
            return res2

# str1: shaoyz
# str2: ao
# dp_array 
# [0, 0]
# [0, 0] s and a: [1][1]=max([1][0], [0][1]);  s and ao: [1][2]=max([1][1], [0][2])
# [0, 0] sh and a; sh and ao
# [1, 1] sha and a; sha and ao
# [1, 2] shao and a; shao and ao
# [1, 2] shaoy and a; shaoy and ao 
# [1, 2] shaoyz and a; shaoyz and ao
# 画
def dp_longest_substring(str1: str, str2: str) -> int:
    str1_len = len(str1)
    str2_len = len(str2)
    dp_array = [[0 for j in range(str2_len + 1)] for i in range(str1_len + 1)]
    
    for i in range(1, str1_len + 1):
        for j in range(1, str2_len + 1):
            if str1[i - 1] == str2[j - 1]:
                dp_array[i][j] = dp_array[i - 1][j - 1] + 1
            else:
                dp_array[i][j] = max(dp_array[i - 1][j], dp_array[i][j - 1])
    return dp_array[str1_len][str2_len]


def test_le():
    str1 = "shaoyz"
    str2 = "ao"
    res = longest_substring(str1, str2)
    print(res)
    str_res = longest_substr(str1, str2)
    print(f"{str1} and {str2} 's longest substr {str_res}")
    dp_res = dp_longest_substring(str1, str2)
    print(f"dp result: {dp_res}")


test_le()
# %%
# constrainted optimization

# %%

def knapsack(weight_value: list, amount: int) -> int:
    if amount <= 0 or len(weight_value) == 0:
        return 0
    print(amount, weight_value)
    if weight_value[-1][0] > amount:
        my_sol = knapsack(weight_value[:-1], amount)
        print(f"my_sol: {my_sol}")
    else:
        sol1 = knapsack(weight_value[:-1], amount)
        sol2 = knapsack(weight_value[:-1], amount - weight_value[-1][0])
        my_sol1 = sol1
        my_sol2 = sol2 + weight_value[-1][1]

        my_sol = max(my_sol1, my_sol2)
    return my_sol


def dp_knapsack(weight_values: list, amount: int) -> int:
    
    pass

def test_knapsack():
    w_v = [(1, 1), (1, 2), (12, 4), (2, 2)]
    res = knapsack(w_v, 15)
    print(res)


test_knapsack()
# %%

# triangle 
def sol_triangle(index: int, triangle: list) -> int:
    # base case
    print(triangle)
    if len(triangle) == 0:
        return 0
    res = []
    if index - 1 >= 0:
        sol1 = sol_triangle(index - 1, triangle[1:]) + triangle[0][index]
        res.append(sol1)
    sol2 = sol_triangle(index, triangle[1:]) + triangle[0][index]
    sol3 = sol_triangle(index + 1, triangle[1:]) + triangle[0][index]
    res.append(sol2)
    res.append(sol3)
    return min(res)


def dp_triangle(triangle: list) -> int:
    r_len = len(triangle)  # rows
    c_len = len(triangle[-1])  # columns
    dp = [[0 for j in range(c_len)] for i in range(r_len)]
    for index, v in enumerate(triangle[-1]):
        dp[-1][index] = v
    print(dp)
    for i in reversed(range(r_len - 1)):
        for index, v in enumerate(triangle[i]):
            sol1 = min(dp[i + 1][index], dp[i + 1][index + 1])
            if index - 1 >= 0:
                if sol1 > dp[i + 1][index - 1]:
                    sol1 = dp[i + 1][index - 1]
            dp[i][index] = sol1 + v
        print(dp)
    return dp[0][0]


def test_sol_triangle():
    triangle = [[2],
                [3, 4],
                [6, 5, 7],
                [4, 1, 8, 3]
                ]
    res = sol_triangle(0, triangle)
    res_dp = dp_triangle(triangle)
    print(f"sol triangle: {res}, dp: {res_dp}")


test_sol_triangle()
# %%

# 爬楼梯 
# 每一次只能上两个台阶 或者 一个台阶
# 大问题分解成小问题
# 第一种情况：这层台阶你是通过一步上来的，这个问题变成了 f(i-1)
# 第二种情况：这层台阶你是通过两步上来的，这个问题变成了 f(i-2)
# 所以问题变成 f(i) = f(i-1) + f(i-2)
# base case: f(1) = 1, f(2) = 2
# base case 解释： 只有1层台阶，:有一种上来的方法
# 有两层台阶：有两种上楼的方法 1+1， 2
