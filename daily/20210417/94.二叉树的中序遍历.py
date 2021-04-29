"""
复习链表 + 二叉树
"""


"""
94. 二叉树的中序遍历
解题思路：递归 和 迭代两种解法
递归解法：
时间复杂度：O(n)
空间复杂度：O(n)
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(root: TreeNode, res: List[int]):
    if root is None: return
    dfs(root.left, res)
    res.append(root.val)
    dfs(root.right, res)


"""
时间复杂度：O(n)
空间复杂度：O(n) 
"""
def dfs(root: TreeNode) -> List[int]:
    if root is None: return []
    stack = []
    res = []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                root = node.right
    return res
