# 前缀和

**  437. 路径总和 III**
**题目描述**
给定一个二叉树，它的每个结点都存放着一个整数值。
找出路径和等于给定数值的路径总数。
路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000]() 的整数。

**解题思路**
```python
437. 路径总和 III
解题思路：前缀和
用hashmap 存储已经遍历的节点的和的个数，key: 节点和，value: 节点和的个数
假设从根节点到当前的节点和为sum_v
路径：     10->5->3->3
节点标记：  1   2  3  4
hash_map = {0: 1, 10: 1, 15: 1, 18: 1}
假设现在遍历到第3个节点，算上该节点的值，sum_v = 15 + 3 = 18
target = 8
sum_v - target = 21 - 8 = 10
13 在hashmap中的value = 1，所以，找到一条路径，路径和与target 一致。
时间复杂度：O(n)
空间复杂度: O(n)
```
**代码**

```python
from collections import defaultdict
def path_sum(root: TreeNode, targetSum: int) -> int:
    # 处理边界条件
    if root is None: return 0
    res = 0
    pre_sum = defaultdict(int)
    pre_sum[0] = 1
    def dfs(root: TreeNode, sum_v: int) -> int:
        nonlocal res
        print(pre_sum)
        if root is None: return 0
        sum_v = sum_v + root.val
        res += pre_sum[sum_v - targetSum]
        pre_sum[sum_v] += 1
        
        dfs(root.left, sum_v)
        dfs(root.right, sum_v)
        pre_sum[sum_v] -= 1
    dfs(root, 0)
    return res

    
```

