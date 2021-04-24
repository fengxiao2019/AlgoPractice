**描述**
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
```c
给定的树 A:

     3
    / \
   4   5
  / \
 1   2
给定的树 B：

   4 
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。
```
B是A的子结构， 即 A中有出现和B相同的结构和节点值。

**代码**
```c
"""
剑指 Offer 26. 树的子结构
解题思路：
边界条件：
A or B 有一个是空树，返回False

子树 检查过程中：
    B先变成None 返回True
    A空，B非空 返回False
    A 非空 B非空  A.val != B.val 返回False
    A 非空 B非空  - 要求B的左子树是A.left的子结构  并且 B的右子树 是A的右子树的子结构
    
判断B是不是A的子结构可以看作是判断
    1. A 和 B是否相等 || A.left 和 B是否相等 || 或者A.right 和 B是否相等
    三者有一个满足就行
    因为是要判断A树是否包含子树，所以，可以针对A的每一个节点重复1

判断B是A的子结构？（根节点相同）
1. A如果先结束  -> return False
2. B先结束 -> True
3. A.val != B.val -> False

dfs(a.left, b.left)  and d

时间复杂度：O(m * n) m 为A树节点数量，n为B树节点数量。
空间复杂度：O(m)
"""


def is_sub_structure(A: TreeNode, B: TreeNode) -> bool:
    if B is None or A is None:
        return False
    
    def dfs(A: TreeNode, B: TreeNode) -> bool:
        
        if B is None: return True
        if A is None: return False
        if A.val != B.val: return False
        
        return dfs(A.left, B.left) and dfs(A.right, B.right)
 
    return dfs(A, B) or is_sub_structure(A.left, B) or is_sub_structure(A.right, B)
```
