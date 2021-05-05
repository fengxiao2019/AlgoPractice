617. 合并二叉树
**描述**
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。
**解题思路**
解题思路：dfs 同时递归遍历两颗树
时间复杂度：O(min(m, n))
空间复杂度：O(min(m,n))
**代码**
```python
def merge_tree(root1: TreeNode, root2: TreeNode)-> TreeNode:
    if not root1 or not root2: return root1 or root2
    new_node = TreeNode(root1.val + root2.val)
    new_node.left = merge_tree(root1.left, root2.left)
    new_node.right = merge_tree(root1.right, root2.right)
    return new_node
```
