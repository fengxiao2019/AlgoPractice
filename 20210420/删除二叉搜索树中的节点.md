450. 删除二叉搜索树中的节点
**题目描述**
给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。
**解题思路**
![][image-1]![][image-2]

case 1: 删除的是叶子节点，直接删除就可以
case 2: 删除的节点存在右子树，用右子树的最小节点替换，删除右子树的最小节点
case 3: 删除的节点只有左子树，用左子树的最大节点替换，删除左子树的最大节点
时间复杂度：O(n)
空间复杂度：O(h)

**代码**
```python

def predecessor(root: TreeNode) -> TreeNode:
    """
    找左子树的最右节点
    """
    root = root.left
    while root.right:
        root = root.right
    return root.val

def successor(root: TreeNode) -> TreeNode:
    """
    找右子树的最左节点
    """
    root = root.right
    while root.left:
        root = root.left
    return root.val

def delete_node(root: TreeNode, key: int) -> TreeNode:
    if root is None: return None
    # 从左子树中删除
    if root.val > key:
        root.left = delete_node(root.left, key)
    # 从右子树中删除
    elif root.val < key:
        root.right = delete_node(root.right, key)
    else:
        # 如果是叶子节点
        if root.left is None and root.right is None:
            root = None
        elif root.right:
            root.val = successor(root)
            root.right = delete_node(root.right, root.val)
        else:
            root.val = predecessor(root)
            root.left = delete_node(root.left, root.val)
    return root
```

[image-1]:	https://tva1.sinaimg.cn/large/008eGmZEly1gpqang6q9vj30s60d4dh3.jpg width=300 height=150
[image-2]:	https://tva1.sinaimg.cn/large/008eGmZEly1gpqantnpatj31b80u00ws.jpg width=300 height=150