组合问题

**39. 组合总和**
**描述**
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。
**说明**
- 所有数字（包括 target）都是正整数。
- 解集不能包含重复的组合。 
例子：
```c
输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]
```

**代码**
```python
"""
解决方法：回溯算法
时间复杂度：O(len(candicates)^target) 松散上限
        更准确的描述：O(len(candicates)^(target/min of candidates))
空间复杂度：O(target) 更准确的描述：O(len(candicates)^(target/min of candidates))
"""

def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    if not candidates: return []
    res = []
    combine = []
    candidates.sort()
    find_numbers(candidates, target, 0 , res, combine)
    return res

def find_numbers(nums: List[int], target: int, start:int, ans: List[List[int]], combine: List[int]) -> None:
    
    if target == 0:
        ans.append(combine[:])
        return
    
    # backtracing
    for i in range(start, len(nums)):
        if target < nums[i]:
            break
        combine.append(nums[i])
        # 数字可以无限制重复被选取，所以下一次的start 还是选择i
        find_numbers(nums, target - nums[i], i, ans, combine)
        combine.pop()
```

**77. 组合**
**描述**
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
eg:
```python
输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
```

**代码**
```python
"""
经典组合问题
解题思路：回溯算法
base case: combine 的长度等于k
时间复杂度：O(n^k)
空间复杂度：O(k)
"""
def combine(n: int, k: int) -> List[List[int]]:
    # define the return result
    res = []
    # tmp combine
    tmp = []
    # backtracking function
    def helper(start: int) -> None:
        # base case
        # len的time complexity is O(1)
        if len(combine) == k:
            res.append(tmp[:])
            return

        for i in range(start, n + 1):
            tmp.append(i)
            helper(i + 1)
            tmp.pop()
    helper(1)
    return res
```

** 216. 组合总和 III**
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
说明：
- 所有数字都是正整数。
- 解集不能包含重复的组合。 
 **代码**
```python
"""
解题思路：回溯
假设用tmp来存储临时的组合，target 为继续要寻找的组和的值
那么backtracking的base base就是：
len(tmp) == k 并且 target == 0

剪裁的部分：如果target 小于下一个要检查的值时，就退出循环，因为后面的值都比target大，不用再继续做下去了
时间复杂度：O()??
空间复杂度：O()??
"""
def combination_sum(k: int, n: int) -> List[List[int]]:
    # result
    res = []
    # tmp result
    tmp = []
    # backtracking fun
    def helper(target: int, start: int):
        if len(tmp) == k:
            if target == 0:
                res.append(tmp[:])
                return
        
        # 开始追溯
        for i in range(start, 10):
            # 剪裁
            if target < i:
                break
            tmp.append(i)
            helper(target - i, i + 1)
            tmp.pop()
    helper(n, 1)
    return res
```

** 17. 电话号码的字母组合**
**描述**
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
![][image-1]
**代码**
```python
"""
hash[2] = 'abc'
hash[3] = 'def'
'23' 相当于 固定住‘2’ -> '3' 
'234' -> 2 - 34 
'34' -> 3 - 4
for item in hash['char']:
    tmp.append(item)
    dfs(digits[1:])
    tmp.pop()

base case: 
    if not digits:
        res.append(tmp[:])

test case: digits 为空： return []
时间复杂度：
空间复杂度：
"""

def letter_combinations(digits: str) -> List[str]:
    # edge case
    if not digits: return []
    # define the return result
    res = []
    # store the tmp result
    tmp = []
    hash_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    # backtracking function
    def helper(index: int) -> None:
        # base case
        if index == len(digits):
            res.append(tmp[:])
            return
        
        characters = hash_map[digits[index]]
        for item in characters:
            tmp.append(item)
            helper(index + 1)
            tmp.pop()
    helper(0)
    return [''.join(item) for item in res]
```
** 40. 组合总和 II**
**描述**
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。
说明：
- 所有数字（包括目标数）都是正整数。
- 解集不能包含重复的组合。 

**代码**
```python
"""
约束条件：
candidates target
candidates 中元素是否都是正数？Y
target 可以为负数吗？N
candidates 可以为空吗？Y
candidates 中的元素可以重复利用吗？ N
candidates 里面的元素有重复吗？ Y
结果集可以重复吗？ N
每个结果中可以有重复的元素吗？每个数字在每个组合中只能使用一次，也就是说如果有重复的元素，就可能在结果中
存在重复的元素
解题思路：利用回溯法
backtracking 退出的条件：
target == 0

剪裁的条件：1. 对candidates 进行排序 2. 如果target < candidates[i], 这个循环就可以退出了，因为后面的元素逗比target 大
3. 因为可能有重复的元素，还需要对重复的元素做一下处理。
时间复杂度：O()
空间复杂度：O()
"""

def combination_sum(nums: List[int], target: int) -> List[List[int]]:
    # process the edge case
    if not nums: return []

    # define the result
    res = []
    # define the tmp result
    tmp = []
    # sort the candidates
    nums.sort()

    def helper(target: int, start: int) -> None:
        if target == 0:
            res.append(tmp[:])
            return

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            if target < nums[i]:
                break
            tmp.append(nums[i])
            helper(target - nums[i], i + 1)
            tmp.pop()

    # backtracking 
    helper(target, 0)
    return res
```

**78 子集**
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
eg: 
```python
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

**代码**
```python
"""
约束条件：
nums 可以为空吗？可以，空返回空
nums 返回的结果集中肯定包含[]
元素互不相同
结果集中不能包含重复的子集
单个结果中不能有重复元素
任意顺序返回
解题思路：
    回溯法
    base case: index == len(nums) : 退出
    进入，就加入到结果集中
    
时间复杂度：O(n*2^n)
空间复杂度：O(n)
"""
def subsets(nums: List[int]) -> List[List[int]]:
    # 处理边界条件
    if not nums: return []
    # 定义返回结果集
    res = []
    # 定义临时结果
    tmp = []
    def helper(index) -> None:
        res.append(tmp[:])
        if index == len(nums):
            return
        for i in range(index, len(nums)):
            tmp.append(nums[i])
            helper(i + 1)
            tmp.pop()
    helper(0)
    return res
```

**897. 递增顺序搜索树**
给你一棵二叉搜索树，请你 按中序遍历 将其重新排列为一棵递增顺序搜索树，使树中最左边的节点成为树的根节点，并且每个节点没有左子节点，只有一个右子节点。
**代码**
```python
"""
解题思路：利用中序遍历的思想
时间复杂度：O(n)
空间复杂度：O(h) h 指树的高度
"""
def increasingBST(root: TreeNode):
    # 定义虚拟节点，保存头部节点
    dummy = TreeNode(-1)
    head = dummy
    def dfs(root: TreeNode):
        nonlocal head
        if not root: return None
        dfs(root.left)
        head.right = root
        root.left = None
        head = head.right
        dfs(root.right)
    dfs(root)
    return dummy.right
```

[image-1]:	https://tva1.sinaimg.cn/large/008i3skNly1gpwf7klw0zj30dv0ckgmk.jpg