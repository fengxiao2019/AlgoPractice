# 1. largest sum contiguous subarray
# %%

# 滑动窗口
# 要解决的是 两个指针的动作
# 左指针的移动规则
# 右指针的移动规则


def largest_sum_c_s_v_1(arr: list) -> int:
    begin, end = 0, 0
    arr_len = len(arr)
    if arr_len == 0:
        return 0
    if arr_len == 1:
        return arr[1]
    max_sum = arr[0]
    for end in range(1, arr_len):
        # 这个涉及到重复计算， 可以使用一个变量保存
        tmp = sum(arr[begin: end + 1])
        print(f"fd  {tmp}")
        if tmp > arr[end]:
            max_sum = tmp
        else:
            max_sum = arr[end]
            begin = end
    return max_sum


# 用一个变量保存a[begin:end+1]之和
def largest_sum_contiguous_subarray(arr: list) -> int:
    arr_len = len(arr)
    if arr_len == 0:
        return 0
    if arr_len == 1:
        return arr[0]

    largest_sum = arr[0]
    win_sum = arr[0]
    begin = 0
    for end in range(1, arr_len):
        # why we need to calculte win_sum?
        # because begin point still with 0
        win_sum = arr[end] + win_sum
        if win_sum < arr[end]:
            largest_sum = arr[end]
            begin = end
            win_sum = arr[end]
        else:
            largest_sum = win_sum
        
        print(f"end: {end}; win_sum: {win_sum}, largest_sum: {largest_sum}")
    print(f"range {begin}: {end+1}")
    return largest_sum


def test_largest_sum():
    arr = [1, -9, 2, 12, 12]
    print(f"original_  {arr}")
    res = largest_sum_contiguous_subarray(arr)
    print(res)
    res1 = largest_sum_c_s_v_1(arr)
    print(res1)


test_largest_sum()


# https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
# 2. maxisize number of 0s by flipping a subarry
def flip(arr: list) -> int:
    arr_len = len(arr)
    zero_size = 0
    max_size = 0
    tmp_max_size = 0
    for i in range(0, arr_len):
        if arr[i] == 0:
            zero_size += 1
            tmp_max_size = 0
        else:
            tmp_max_size += 1
            if tmp_max_size > max_size:
                max_size = tmp_max_size
    return zero_size + max_size


def flip_version_1(arr: list) -> int:
    arr_len = len(arr)
    zero_size = 0
    max_size = 0
    begin, end = 0, 0
    for end in range(0, arr_len):
        if arr[end] == 0:
            zero_size += 1
            begin = end
        else:
            if end - 1 >= 0 and arr[end - 1] == 0:
                begin = end
            
            window_size = end - begin + 1
            if window_size > max_size:
                max_size = window_size
    return zero_size + max_size


flip_arr = [[1, 0], [0, 1], [1], [0], [0, 0, 1, 0, 1, 1, 0]]


for item in flip_arr:
    res = flip(item)
    res1 = flip_version_1(item)
    print(res, res1)
    assert(res == res1)

# https://www.geeksforgeeks.org/maximize-number-0s-flipping-subarray/
# 3. house robber
#      0  1  2  3   4  5
# eg: [5, 9, 4, 1, 12, 8]
# 分析

# f(0) = max(f(2) + 5, f(1)) = max(16+5, 21) = 21
# f(1) = max(f(3) + 9, f(2)) = max(12+9, 16) = 21
# f(2) = max(f(4) + 4, f(3)) = max(12+4, 12) = 16
# f(3) = max(f(5) + 1, f(4)) = max(8+1, 12) = 12
# f(4) = max(12, 8) = 12
# f(5) = 8
# so f(i) = max(f(i+2) + arr[i], f(i+1))

# recursive
def house_robber(arr: list) -> int:
    arr_len = len(arr)
    if arr_len <= 2:
        return max(arr)
    sol1 = house_robber(arr[1:])
    sol2 = house_robber(arr[2:]) + arr[0]
    return max(sol1, sol2)

# dp
def dp_house_robber(arr: list) -> int:
    arr_len = len(arr)
    if arr_len <= 2:
        return max(arr)

    dp_array = [0 for item in range(arr_len)]
    dp_array[0] = arr[0]
    dp_array[1] = max(arr[0], arr[1])
    for i in range(2, arr_len):
        dp_array[i] = max(dp_array[i - 2] + arr[i], dp_array[i - 1])
    return dp_array[arr_len - 1]

robber_arr = [5, 9, 4, 1, 1, 2]
res = house_robber(robber_arr)
res2 = dp_house_robber(robber_arr)
print(f"robber: {res}: dp_res: {res2}")
assert(res == res2)


# 4. minimum window substring
"""
eg: s = "ABOBECODEBANG" T="ABC"
output: "BANC"
solution:
origin = dict() 
for i in T:
    if i in origin:
        origin[i] += 1
    else:
        origin[i] = 0
"""


def m_w_s(s: list, t: list) -> int:
    origin = dict()
    for item in t:
        if item in origin:
            origin[item] += 1
        else:
            origin[item] = 1
    if not origin:
        return ""

    begin = 0
    min_v = s
    for end in range(0, len(s)):
        print(f"origin: {origin}")
        if s[end] in origin:
            origin[s[end]] -= 1
        count = [1 for item in origin.values() if item > 0]
        while not count:
            print(origin, begin, end)
            if len(min_v) > end - begin + 1:
                min_v = s[begin: end + 1]
            if s[begin] in origin:
                origin[s[begin]] += 1
            begin += 1
            count = [1 for item in origin.values() if item > 0]
    return min_v

str1 = "ABOBECODEBANC"
str2 = "ABC"
res = m_w_s(str1, str2)
print(res)


# 5. rainwater
"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
"""


# 6. sorted two sum
"""
input array: arr = [10, 22, 28, 29, 30, 40]
x: 54
prob1: find the pair in the array whose sum is closest to x
    solution:
    i = 0, j = 5 => a[i] + a[j] = 50 < x => i = i+1; min = x - 50 = 4
    i = 1, j = 5 => a[i] + a[j] = 62 > x => j = j-1; min = min(62-x, 4) = 4
    i = 1, j = 4 => a[i] + a[j] = 52 < x => i = i+1; min=min(abs(52-x),4)=2
    i = 2, j = 4 => a[i] + a[j] = 58 > x => j = j-1; min=min(58-x,2)=2
    i = 2, j = 3 => a[i] + a[j] = 57 > x => j = j-1; min=min(57-x,2)=2
    i = 2, j = 2 => break, j must greater than 2

prob2: find the pair in the array whose sum is equal to x
solution:
    i = 0 -> n, x - a[i] in hash: return true else hash[v] = 1
"""

### slow and fast pointer
# Given an array of integers of size 'n'
# Our aim is to calculate the maximum sum possible for 'k' consecutive elements in the array
# input : arr[] = {100, 200, 300, 400} k=2
# output : 700
# %%
# window with the fixed size
def max_sum_k(arr: list, k: int) -> int:
    arr_len = len(arr)
    if arr_len <= k:
        return sum(arr)

    wind_sum = sum(arr[0:k])  # memory the last summary
    max_sum = wind_sum
    for i in range(arr_len):
        j = i + k
        if j >= arr_len:
            break
        wind_sum += arr[j] - arr[i]
        max_sum = max(max_sum, wind_sum)
    return max_sum


def test_max_sum_k():
    arr = [1, 0, 12, -1, -19, 30]
    k = 4
    res = max_sum_k(arr, k)
    print(res)


test_max_sum_k()


# 7. finding all anagrams in a string
"""
Input:  txt[] = "BACDGABCDA"  pat[] = "ABCD"
   Output:   Found at Index 0
             Found at Index 5
             Found at Index 6
# slide window + anagrams 的判断
# 
eg : ascii 256
arr = [0 for i in range(256)]
arr[ord('B')]=1
arr[ord('A')]=1
arr[ord('C')]=1
arr[ord('D')]=1
slide window 
"""

# 8. substring with concatenation of all words
"""
note: the same length
Input : S: "barfoothefoobarman"
        L: ["foo", "bar"]
Output : 0 9
Explanation: 
// at index 0 : barfoo
// at index 9 : foobar

solution: hash store the words in L, the key is word and the value is frequency in L
eg: hash['foo'] = 1, hash['bar'] = 1;
fixed_window size = len(L) * len(L[0])
step = len(L[0])
all the values in hash is zero indicate the substring is the concatenation of L
"""
# 9. longest substring without repeating characters
"""


look for the pattern
       01234567
input: AABCDCEF
直观思路：
A
AB
ABC
ABCD
DC
DCE
DCEF

关联上索引
(1) i=0, j=0 => A
(2) i=1,j=1 => A #  i: 0->1
(3) i=1, j=2 => AB
(4) i=1, j=3 => ABC
(5) i=1, j=4 => ABCD
(6) i=4, j=5 => DC   # i: 1->4
(7) i=4, j=6 => DCE
(8) i=4, j=7 => DCEF

在第二步和第6步，i的值发生了变化

? 什么时间i 变更？如何变更？
用hash记录每个字符最近出现的位置
当a[j] in hash



"""

# 10 longest substring with at most two distinct characters

# 11 longest substring with at most k distinct characters

# 11. permutation in string

# 13. longest repeating character replacement
