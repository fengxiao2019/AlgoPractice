Monotonic Stack
**定义**
单调栈 是一种栈并且栈内元素必须保持单调，具体来说就是入栈时通过弹出原素来保持栈的单调性，通常分为两种：单调递增栈 和 单调递减栈。
单调递增栈：从栈顶到栈低的元素是严格递增的。
单调递减栈：从栈顶到栈低的元素是严格递减的。
**用途**
通常用来解决线性数据结构中 [下一个/上一个] [更大/更小] 的元素。
- 寻找   `更大`的元素，使用单调递增栈。
```python
    # 下一个更大
	from typing import List
	def findNextGreater(nums: List[int]) -> List[int]:
		stack = []
		ans = [-1] * len(nums)
		for i, v in enumerate(nums):
	    	while stack and nums[stack[-1]] < v:
	        	top_i = stack.pop()
	        	ans[top_i] = v
	    	stack.append(i)
		return ans
```
- 寻找`更小`的元素，使用单调递减栈。
```python
	# 下一个更小
	def findNextSmaller(nums: List[int]) -> List[int]:
		stack = []
		ans = [-1] * len(nums)
		for i, v in enumerate(nums):
    		while stack and nums[stack[-1]] > v:
        		top_i = stack.pop()
        		ans[top_i] = v
    		stack.append(i)
		return ans
```
- 寻找 `下一个` 的元素，从左往右遍历。
```python
	# 上一个更大
	def findPreviousGreater(nums: List[int]) -> List[int]:
		stack = []
		ans = [-1] * len(nums)
		for i in range(len(nums) - 1, -1, -1):
	    	v = nums[i]
	    	while stack and nums[stack[-1]] < v:
	        	top_i = stack.pop()
	        	ans[top_i] = v
	    	stack.append(i)
		return ans
	

```
- 寻找 `上一个`的元素， 从右往左遍历。
	```python
	# 上一个更小
	def findPreviousSmaller(nums: List[int]) -> List[int]:
		stack = []
		ans = [-1] * len(nums)
		for i in range(len(nums) - 1, -1, -1):
	    	v = nums[i]
	    	while stack and nums[stack[-1]] > v:
	        	top_i = stack.pop()
	        	ans[top_i] = v
	    	stack.append(i)
		return ans

	```
**基础题**
**496. 下一个更大元素 I**
> 给你两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。
> 请你找出 nums1 中每个元素在 nums2 中的下一个比其大的值。
> nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。
```python
"""
解题思路：单调栈 + hash表
遍历一遍nums2 获取每个元素的下一个更大元素，用hash表存储，k为对应值，val 为对应的下一个更大元素
遍历一遍nums1，结合hash表获取结果
时间复杂度：O(n)
空间复杂度：O(n)
"""
def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    stack = []
    hash_map = {}
    for i in range(len(nums2)):
        while  stack and stack[-1] < nums2[i]:
            hash_map[stack[-1]] = nums2[i]
            stack.pop()
        stack.append(nums2[i])
    res = []
    for item in nums1:
        res.append(hash_map.get(item, -1))
    return res
```

**739. Daily Temperatures**
> Given a list of daily temperatures temperatures, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

> For example, given the list of temperatures temperatures = [73, 74, 75, 71, 69, 72, 76, 73](), your output should be [1, 1, 4, 2, 1, 1, 0, 0]().

> Note: The length of temperatures will be in the range [1, 30000](). Each temperature will be an integer in the range [30, 100]().
```python
"""
思路：
可以利用stack解决该问题

[73, 74, 75, 71, 69, 72, 76, 73]

抽象：
结果集为 [0] * len(temperatures)
stack 存储下标，默认为[]
当前温度比stack顶下标指向的温度高：更新结果集中对应下标 val：cur - stack[-1]

边界条件检查：
温度为空： 空
温度长度为1: [0]
检查抽象过程是否能够覆盖这两个边界条件

复杂度：
时间复杂度：O(n)
空间复杂度：O(n)
"""

def dailyTemperatures(temperatures: List[int]) -> List[int]:
    ans = [0] * len(temperatures)
    stack = []
    i = 0
    while i < len(temperatures):
        if stack and temperatures[i] > temperatures[stack[-1]]:
            peek = stack.pop()
            ans[peek] = i - peek
        else:
            stack.append(i)
            i += 1
    return ans
```

**1124. Longest Well-Performing Interval**
> We are given hours, a list of the number of hours worked per day for a given employee.
> A day is considered to be a tiring day if and only if the number of hours worked is (strictly) greater than 8.
> A well-performing interval is an interval of days for which the number of tiring days is strictly larger than the number of non-tiring days.
> Return the length of the longest well-performing interval.
```python
"""
[9, 9, 6, 0, 6, 6, 9]
用+1分 表示当天工作时间超过8个小时
用-1分 表示当天工作时间小于8个小时
这样变成[1, 1, -1, -1, -1, -1, 1]
前缀和： [1, 2, 1, 0, -1, -2, -1]

如果 下标i 对应的score > 0，最长连续天数 <= i + 1的，所以ans = i + 1
如果下标i 对应的score < 0，转变成求最长子序列的和为1的问题
参考问题：

用一个hash 表记录所有的score
时间复杂度：O(n)
空间复杂度：O(n)

"""

def longestWPI(hours):
    hash_map = {}
    ans = 0
    score = 0
    for i, h in enumerate(hours):
        score += 1 if h > 8 else -1
        if score > 0:
            ans = i + 1
        else:
            if score - 1 in hash_map:
                ans = max(ans, i - hash_map[score - 1])
        hash_map.setdefault(score, i)
    return ans

```
**402. Remove K Digits**
```python
"""
解题思路：
ABCDEF
如果B对应的值小于A对应的值=>BCDEF < ACDEF
如果C对应的值小于min(A,B), -> CDEF
对DEF执行同样的操作，可以看出，这是一个单调栈递增栈的题目
while stack and stack[-1] > item:
    stack.pop()
stack.append(item)

边界条件：
    k == 0: 返回 num
    num 为空，返回空
    k >= len(num): 返回空
复杂度：
时间复杂度：O(n)
空间复杂度：O(n)
"""

def removeKdigits(num: str, k: int) -> str:
    stack = []
    left_l = len(num) - k
    i = 0
    for item in num:
        while stack and stack[-1] > item and k > 0:
            stack.pop()
            k -= 1
        stack.append(item)
    return "".join(stack[:left_l]).lstrip("0") or "0"
```
**316. Remove Duplicate Letters **
> Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

```python
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count_dict = Counter(s)  # count the number of times the character appears
        stack = []
        for item in s:
            if item not in stack:
                while stack and stack[-1] > item and count_dict[stack[-1]] > 0:
                    stack.pop()
                stack.append(item)
            count_dict[item] -= 1
        return "".join(stack)

```

**907. Sum of Subarray Minimums**
> Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

```python
"""
解题思路：单调递增栈
3   1   2   4
sum(min(b)) = f(i) * nums[i]  i = 0 1 2  ... n-1
f(i) 表示以nums[i]为最小值的子数组的个数

怎么确定以nums[i] 为子数组的个数？

3  1   2    4 
0  1   2    3
   ^   *       ^
对于下标为2的元素，ple（previous less number） 是1
                nle (next less number) 不存在，相当于len(nums)
ple ~ 2 的距离 dis_ple 为 2 - 1 = 1
2 ～ nle 的距离 dis_nle 为 4 - 2 = 2
2
2 4

因此2 对结果的贡献为：2 * (dis_ple * dis_nle) = 2 * (1 * 2) = 4
对于nums[i] 对结果的贡献为：nums[i] * ((i - ple) * (nle - i))
复杂度：
时间复杂度：O(n)
空间复杂度：O(n)
"""

def sumSubarrayMins(arr: List[int]) -> int:
    previous_res = previous_less_index(arr)
    next_res = next_less_index(arr)
    sum_v = 0
    for i in range(len(arr)):
        pre_dis = i - previous_res[i]
        next_dis = next_res[i] - i
        
        sum_v += arr[i] * (next_dis * pre_dis)
    return sum_v % (pow(10, 9)+7)



def previous_less_index(arr: List[int]) -> List[int]:
    stack = []
    previous_res = [-1] * len(arr)
    for i in range(len(arr)):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        if stack:
            previous_res[i] = stack[-1]
        stack.append(i)
    return previous_res


def next_less_index(arr: List[int]) -> int:
    stack = []
    next_res = [len(arr)] * len(arr)
    for i in range(len(arr)):
        while stack and arr[stack[-1]] > arr[i]:
            next_res[stack[-1]] = i
            stack.pop()
        stack.append(i)
    return next_res
```
**901. 股票跨度**
> 编写一个 StockSpanner 类，它收集某些股票的每日报价，并返回该股票当日价格的跨度。
> 今天股票价格的跨度被定义为股票价格小于或等于今天价格的最大连续日数（从今天开始往回数，包括今天）。
> 例如，如果未来7天股票的价格是 [100, 80, 60, 70, 60, 75, 85]()，那么股票跨度将是 [1, 1, 1, 2, 1, 4, 6]()。

```python
class StockSpanner:
    """
    用一个栈维护一个单调递减的栈，通过栈来跟踪span
    记录每个元素的跨度
    当压入100 时，因为stack 为空，返回 1
    span[0] = 1
    stack = [(0,100)]
    当压入80 时，stack[-1] > 80,压入80
    stack = [(0, 100), (1, 80)]
    span[1] = 1
    当压入 60， stack[-1] > 60,压入60
    stack = [(0,100), (1, 80), (2, 60)]
    span[2] = 60
    当压入70， stack[-1] <= 70, 弹出60 
    stack = [(0, 100), (1, 80), (3, 70)]
    span[3] = 2
    ...
    """
    def __init__(self):
        # 用栈存储当前价格走势，维护一个递减栈
        self.stack = []
        # 默认的跨度为1
        self.span = []


    def next(self, price: int) -> int:
        index = len(self.span)
        span_val = 1
        while self.stack and self.stack[-1][1] <= price:
            top_index, _ = self.stack.pop()
            span_val += self.span[top_index]
        self.stack.append((index, price))
        self.span.append(span_val)
        return self.span[-1]
```

** 856. Score of Parentheses**
> Given a balanced parentheses string s, compute the score of the string based on the following rule:
> > - () has score 1
> > - AB has score A + B, where A and B are balanced parentheses strings.
> > - (A) has score 2 * A, where A is a balanced parentheses string.
```python
class Solution:
    """
    思路：（ => 入栈
          ) => 
            1. ( => if score == 0: score = 1 else: score = 2 * score
            2. score += val
            3. 入栈
        结果：sum stack
    """
    def scoreOfParentheses(self, s: str) -> int:
        if not s: return 0
        stack = []
        for item in s:
            if item == ')':
                score = 0
                while stack and stack[-1] != '(':
                    score += stack.pop()
                
                if score == 0:
                    score = 1
                else:
                    score = 2 * score
                stack.pop() # 弹出最后一'('
                stack.append(score)
            else:
                stack.append(item)
        return sum(stack)
```
** 503. Next Greater Element II**
> Given a circular integer array nums (i.e., the next element of nums[nums.length - 1]() is nums[0]()), return the next greater number for every element in nums.
> The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.
```python
"""
解题思路：扩展nums为 nums + nums，这样每个元素都能够找到比他大的下一个元素
res = [-1] * len(nums)
这样，我们不用处理找不到比当前元素大的元素
对于扩展后的下标：对应的实际下标为 i % len(nums)
为了找到比当前元素大的下标，实际上是在维护一个递减栈
时间复杂度：O(n)
空间复杂度：O(n)
"""

def nextGreaterElements(nums: List[int]) -> List[int]:
    length = len(nums)
    nums = nums + nums
    res = [-1] * length
    stack = []
    for i in range(length + length):
        while stack and nums[stack[-1]] < nums[i]:
            val = stack.pop()
            res[val] = nums[i]
        stack.append(i % length)
                
    return res
```

** 84. Largest Rectangle in Histogram**
> Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        return largestRectangleArea(heights)

"""
以2 1 5  为例，为了方便计算，我们在数组左右两边各设置一个哨兵
  0   2    1     5   0

  一根柱子能决定的最大面积取决于左边比它矮的元素i 和 右边比他矮的元素j
  (j - i - 1) * h 就是能够决定的面积

  寻找比左边比m小的元素，可以使用单调递增栈
  
  时间复杂度：O(n)
  空间复杂度：O(n)
"""

def largestRectangleArea(heights: List[int]) -> int:
    heights = [0] + heights + [0]
    stack = [0]
    n = len(heights)
    max_area = 0
    for i in range(1, n):
        while stack and heights[stack[-1]] > heights[i]:
            cur = stack.pop()
            # 计算高度 
            h = heights[cur]
            while stack and heights[stack[-1]] == h:
                cur = stack.pop()
            # 计算宽度
            if stack:
                w = i - stack[-1] - 1
            else:
                w = i - cur
            max_area = max(w * h, max_area)
        stack.append(i)
    return max_area
```
**接雨水**
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
```python
class Solution:
    def trap(self, height: List[int]) -> int:
        return trap(height)
"""

stack 维护一个单调递减栈（非严格单调），这样左边的元素都比stack[-1]大，碰到右边的元素比stack[-1]大的元素，就可以计算
stack[-1] 贡献的水量大小
逐个对stack中的每个元素计算贡献水量，所有水量的大小就是结果
场景1:
44444 6 这种-> 0
54333 6 这种  计算 3  4  5

时间复杂度：O(n)
空间复杂度：O(n)
"""

def trap(height: List[int]) -> int:
    n = len(height)
    if n <= 2: return 0

    stack = [0]
    ans = 0
    for i in range(1, n):
        while stack and height[stack[-1]] < height[i]:
            cur_index = stack.pop()
            if stack:
                left_bound = stack[-1]
                h = min(height[left_bound], height[i]) - height[cur_index]
                w = i - left_bound - 1
                ans += w * h
        stack.append(i)   
    return ans
```

