

"""
后序遍历：递归方法
时间复杂度：O(n)
空间复杂度：O(h)
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorderTraversal(root: TreeNode) -> List[int]:
    res = []
    def dfs(root: TreeNode):
        if not root:
            return
        dfs(root.left)
        dfs(root.right)
        res.append(root.val)
    dfs(root)
    return res


"""
迭代法
时间复杂度：O(n)
空间复杂度：O(n)
"""

def postorderTraversal(root: TreeNode) -> List[int]:
    stack = []
    ans = []
    last_visited = None
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            peek = stack[-1]
            if peek.right and last_visited != peek.right:
                root = peek.right
            else:
                res = stack.pop()
                last_visited = res
                ans.append(res.val)
    return ans

"""
迭代法
nrl 翻转 => lrn
时间复杂度：O(n)
空间复杂度：O(n)
"""

def postorderTraversal(root: TreeNode) -> List[int]:
    if not root: return []
    stack = [root]
    ans = []
    while stack:
        node = stack.pop()
        ans.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return ans[::-1]