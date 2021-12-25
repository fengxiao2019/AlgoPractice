538. 把二叉搜索树转换为累加树

**描述**
给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。

提醒一下，二叉搜索树满足下列约束条件：

节点的左子树仅包含键 小于 节点键的节点。
节点的右子树仅包含键 大于 节点键的节点。
左右子树也必须是二叉搜索树。
![][image-1]
**解题**
```python
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        """
        解题思路：利用中序遍历RNL
        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        stack = []
        sum_v = 0
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.right
            else:
                peek = stack.pop()
                sum_v += peek.val
                peek.val = sum_v
                node = peek.left
        return root
```

[image-1]:	https://tva1.sinaimg.cn/large/008i3skNly1gprs0tmgjmj30lj0epjs2.jpg