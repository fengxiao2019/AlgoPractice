"""
98. 验证二叉搜索树
解题思路：
以root 为根节点的树是二叉搜索树
必须满足：
root.left 是二叉搜索树
root.right 是二叉搜索树
子树   大于最小值
      小于最大值

边界条件：空节点 返回 False

退出条件：叶子节点 返回True，最大值返回节点val
"""

import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: TreeNode) -> bool:
    # 处理边界条件
    if root is None: return False

    def dfs(root: TreeNode, min_v: int, max_v: int) -> int:
        if root is None:
            return True
        if root.val >= max_v or root.val <= min_v:
            return False
        left = dfs(root.left, min_v, root.val)
        right = dfs(root.right, root.val, max_v)
        return left and right
    return dfs(root, -sys.maxsize, sys.maxsize)
