# palindrome

## 回文串的特征
1. 最多有一个字符出现奇数次
2. 左半部分和右半部分完全相等
## 题目类型1 - 验证回文串
[125. 验证回文串][1]
只考虑字符串中的字母和数字，忽略大小写
```python
"""
回文串验证，利用特征：左半部分和右半部分完全相等
双指针
时间复杂度：O(n)
空间复杂度：O(1)
"""
def isPalindrome(s: str) -> bool:
    if len(s) <= 1: return True

    l, r = 0, len(s) - 1
    while l < r:
        if not check_vaild(s[l]):
            l += 1
            cotinue
        if not check_vaild(s[r]):
            r -= 1
            continue
        
        if l > r:
            break
        
        if s[l].lower() == s[r].lower():
            l += 1
            r -= 1
        else:
            return False
    return True

def check_vaild(s: str) -> bool:
    return s.isalnum()
```

[234. 回文链表][2]
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        return is_palindrome(head)


"""
234. 回文链表
# 思路  
步骤1: 从中间断开，变成两个链表 l 和 r 
步骤2: 翻转链表r
步骤3: 检查r和l是否一致，退出条件是r 结束

边界条件处理：
1. 链表为空  返回False
2. 链表长度为1 返回 True

当链表的长度为偶数时，l的长度 == r的长度
当链表的长度为奇数时，l的长度 == r的长度 + 1
#
"""
# 分割链表
def split_link(head):
    if not head or head.next is None:
        return head, None
    
    slow, fast = head, head
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    left = head
    right = slow.next
    slow.next = None
    return left, right

#翻转链表
def reverse_link(head):
    if not head or head.next is None:
        return head
    pre = None
    while head:
        tmp = head.next
        head.next = pre
        pre = head
        head = tmp
    return pre

# 检查链表是否相等

def check_same(l1: ListNode, l2: ListNode) -> bool:
    while l2 and l1:
        if l1.val == l2.val:
            l1 = l1.next
            l2 = l2.next
        else:
            return False
    return True

def is_palindrome(head: ListNode) -> bool:

    l, r = split_link(head)
    r = reverse_link(r)
    return check_same(l, r)
```

[**128. 破坏回文串**][3]
给你一个回文字符串 palindrome ，请你将其中 一个 字符用任意小写英文字母替换，使得结果字符串的字典序最小，且 不是 回文串。
请你返回结果字符串。如果无法做到，则返回一个空串。
```python
class Solution:
    """
    特殊情况：palindrome 长度如果为1，怎么折腾都是回文串
    字典序最小，因为是回文串，前半部分和后半部分相等，所以只需要关心前半部分就行。
    如果是奇数长度的回文串，中间的字符你怎么换还是回文串，所以，不用管中间的字符
    如果前半部分没找到非a的字符，说明，前半部分都是a，后半部分也都是a，那直接将字符串的最后一个字符设置成‘b’
    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        for i in range(len(palindrome)//2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]
        return palindrome[:-1] + 'b'     
```

[680. 验证回文字符串 Ⅱ][4]
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
利用特征：左半部分和右半部分完全相等
```python
"""
时间复杂度：O(n)
空间复杂度:O(n)
"""
def validPalindrome(s: str) -> bool:
    i = 0
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            break
    if left >= right:
        return True
    return isPalindrome(s[left+1: right+1]) or isPalindrome(s[left: right])

def isPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```

[266. 回文排列][5]
给定一个字符串，编写一个函数判定其是否为某个回文串的排列之一。
回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。
回文串不一定是字典当中的单词。
```python
class Solution:
    """
    统计每个字符出现的次数
    累加偶数个出现次数的字符，结果为sum_count
    如果sum_count == len(s) 或者 sum_count + 1 == len(s)，说明可以通过重新排列组合成回文串
    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    def canPermutePalindrome(self, s: str) -> bool:
        char_count = collections.Counter(s)
        sum_count = 0
        for v in char_count.values():
            if v % 2 == 0:
                sum_count += v
            else:
                sum_count += v - 1
        return sum_count == len(s) or sum_count + 1 == len(s)
```
[1332. 删除回文子序列][6]
给你一个字符串 s，它仅由字母 'a' 和 'b' 组成。每一次删除操作都可以从 s 中删除一个回文 子序列。返回删除给定字符串中所有字符（字符串为空）的最小删除次数。
```python
class Solution:
    """
    如果s 本身是回文串，一步就删除完
    否则，至少两步：第一步：先删所有的a ；第二步：删除所有的b
    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    def removePalindromeSub(self, s: str) -> int:
        if s == s[::-1]: return 1
        return 2
```
[9. 回文数][7]
或者是转成字符串判断
```python
def isPalindrome(x: int) -> bool:
    if x < 0: return False
    z = x
    palindrome_val = 0
    while z:
        palindrome_val = palindrome_val * 10 + z % 10
        z = z // 10
    return x == palindrome_val
```
## 题目类型2 - 寻找最长回文串，寻找最长回文子序列
这类题目基本都是dp解法，而且状态方程基本一致
dp[i][j] 和 dp[i+1][j-1]之间的关系
dp[i][j] 和 dp[i+1][j] 和 dp[i][j-1]之间的关系
以寻找最长回文串为例
先定义状态转移方程，因为是要返回的是最长回文子串
dp[i][j] 定义为s[i:j+1]是否是一个回文串
状态转移方程：
当s[i] == s[j]时，
	dp[i][j] = dp[i+1][j-1]
每一次遍历更新begin 和 max_len 

[5. 最长回文子串][8]
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        return longestPalindrome(s)

"""
动态规划解法
如果s[i] == s[j]:
    dp[i][j] = dp[i+1][j-1]
长度为1 都是回文串
dp[i][i] = True
长度为2的需要看dp[i][i+1] s[i] == s[i+1]
"""

def longestPalindrome(s: str) -> str:
    n = len(s)
    if n <= 1: return s
    dp = [[False] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = True
    
    max_len = 1
    begin = 0
    # 处理长度为>=2的回文串
    # 最长为整个数组
    for l in range(2, len(s) + 1):
        for i in range(n):
        # l = j - i + 1
            j = l + i - 1
            if j >= n:
                break
            if s[i] == s[j]:
                if l == 2:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i+1][j-1]
        
            if dp[i][j] and max_len < l:
                max_len = l
                begin = i
    return s[begin: begin + max_len]
```
[516. 最长回文子序列][9]
要求返回的是长度
```python
class Solution:
    """
    最长回文子序列，类似最长回文子串
    状态：dp[i][j] 表示s[i:j+1]范围内最长回文串的长度
    转移方程：
        如果s[i] == s[j]
            dp[i][j] = dp[i+1][j-1] + 2
        否则：
            dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    初始化：
        dp[i][i] = 1
    返回的结果：dp[0][n-1]
    
    时间复杂度：O(n^2)
    空间复杂度：O(n^2)
    """
    def longestPalindromeSubseq(self, s: str) -> int:
        # 定义dp
        if not s: return 0
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        
        # 自低向上
        # for j in range(len(s)):
        #     for i in range(j-1, -1, -1):
        
        # 自顶向下
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    dp [i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][len(s) - 1]
```

1682. 最长回文子序列 II
```python
class Solution:
    """
    dp[i][j]存储的s[i:j+1] 范围内的最长的偶数回文子序列的长度+结尾字符
	之前为了求子序列最大值，初始化了dp[i][i] = 1,求偶数时就不需要了，这样求出来的就是最大偶数长度的回文子序列了
    
    时间复杂度：O(n^2)
    空间复杂度：O(n^2)
    """
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s: return 0
        # 定义dp
        dp = [ [[0, '']] * len(s) for _ in range(len(s))]
		
        for i in range(len(s) - 1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j] and dp[i+1][j-1][1] != s[i]:
                    dp[i][j][1] = s[i]
                    dp[i][j][0] = dp[i+1][j-1][0] + 2

```
647. 回文子串
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。
```python
class Solution:
    """
    if s[i] == s[j]:
        dp[i][j] = dp[i-1][j-1]
    如果 s的长度为1: 返回 1
    状态:dp[i][j] 表示s[i:j+1]是否是回文串
	转移方程： dp[i][j] = dp[i+1][j-1] 如果s[i] == s[j]
    时间复杂度：O(n^2)
    空间复杂度：O(n^2)
    """
    def countSubstrings(self, s: str) -> int:
        if len(s) <= 1: return len(s)
        
        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        
        count = len(s)
        for l in range(2, len(s) + 1):
            for i in range(len(s)):
                # l = j - i + 1
                j = l + i - 1
                if j >= len(s):
                    continue
                if s[i] == s[j]:
                    if l == 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                # 统计回文子串的个数
                if dp[i][j]:
                    count += 1
        return count
```

[267. 回文排列 II][10]
给定一个字符串 s ，返回其通过重新排列组合后所有可能的回文字符串，并去除重复的组合。
如不能形成任何回文排列时，则返回一个空列表。
```python
class Solution:
    """
    如果每个排列都验证是否是回文，会超时
    先判断字符串能否通过排列变成回文字符串，如果不能，返回空串
    可以这么干，只排列一半，把另一半复制上
    如果是奇数长度的字符串，把多出来的那个字符复制的时候添加上
    时间复杂度：O(n*n!)
    空间复杂度：O(n)
    """
    def generatePalindromes(self, s: str) -> List[str]:
        char_counter = Counter(s)
        half = []
        odd_key = ""
        # 找一半的字符
        for key in char_counter:
            if char_counter[key] % 2 == 1:
                odd_key = key
            for i in range(char_counter[key] // 2):
                half.append(key)
        # 验证字符串能否通过排列构成回文串
        print(half)
        if len(half) * 2 != len(s) and len(half) * 2 + 1 != len(s):
            return []
        
        # 开始排列
        ans = []
        compose = []
        visited = defaultdict(bool)
        def dfs(arr: List[str]) -> None:
            if len(compose) == len(arr):
                str_half = "".join(compose)
                ans.append(str_half + odd_key + str_half[::-1])
                return
            for i in range(len(arr)):
                if visited[i]:
                    continue
                if i > 0 and arr[i] == arr[i-1] and not visited[i-1]:
                    continue
                compose.append(arr[i])
                visited[i] = True
                dfs(arr)
                compose.pop()
                visited[i] = False
        dfs(half)
        return ans
```
## 题目类型3 - 寻找所有的回文串，寻找所有回文子序列
## 题目类型4 - 分割回文串

[1]:	https://leetcode-cn.com/problems/valid-palindrome/
[2]:	https://leetcode-cn.com/problems/palindrome-linked-list/
[3]:	https://leetcode-cn.com/problems/break-a-palindrome/
[4]:	https://leetcode-cn.com/problems/valid-palindrome-ii/
[5]:	https://leetcode-cn.com/problems/palindrome-permutation/
[6]:	https://leetcode-cn.com/problems/remove-palindromic-subsequences
[7]:	https://leetcode-cn.com/problems/palindrome-number/
[8]:	https://leetcode-cn.com/problems/longest-palindromic-substring/
[9]:	https://leetcode-cn.com/problems/longest-palindromic-subsequence/
[10]:	https://leetcode-cn.com/problems/palindrome-permutation-ii/