78. Subsets
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
例子：
```python
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

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
    ans = []
    combine = []
    def dfs(index: int) -> None:
        ans.append(combine[:])
        if index == len(nums): return
        for i in range(index, len(nums)):
            combine.append(nums[i])
            dfs(i + 1)
            combine.pop()
    dfs(0)
    return ans


"""
[1,2,3] 集合的个数为2^3
三个bit能够表达的数量大小也是2^3
可以用每个位上的bit的状态模拟下标元素是否存在
eg: 5 = 101
检查 101 & 1 << 2 = 1
    101 & 1 << 1 = 0
    101 & 1 << 0 = 1
时间复杂度：O(n)
空间复杂度：O(1)
"""

def subsets(nums: List[int]) -> List[List[int]]:
    if not nums: return []
    mask = pow(2,len(nums))
    ans = []
    for j in range(mask):
        tmp = []
        for i in range(0, len(nums)):
            if j & (1 << i):
                # print(mask-1-i)
                tmp.append(nums[i])
        ans.append(tmp[:])
    return ans
```

