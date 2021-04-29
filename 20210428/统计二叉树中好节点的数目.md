1448. 统计二叉树中好节点的数目
**描述**
给你一棵根为 root 的二叉树，请你返回二叉树中好节点的数目。
「好节点」X 定义为：从根到该节点 X 所经过的节点中，没有任何节点的值大于 X 的值
**解题思路**
传入两个参数：一个是root  从根节点到当前节点路径上的最大值max_v
if root.val \>= max_v: 就累加一个节点

继续在左子树和右子树上判断
时间复杂度：O(n)
空间复杂度：O(h)
**代码**
```python
def goodNodes(root: TreeNode, max_v: int) -> int:
    if root is None: return 0
    res = 0
    if root.val >= max_v:
        max_v = root.val
        res = 1

    left = goodNodes(root.left, max_v)
    right = goodNodes(root.right, max_v)
    res += left
    res += right
    return res
```

