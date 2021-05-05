#270. Closest Binary Search Tree Value
# Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.

"""
if root.val == target:
    # 找到了target，返回target
root.val > target: 说明右边的值都不会是最接近target的值
    ->root.left
else
                   说明左边的值都不会是最接近target的值
base case：
    if abs(root.val - target) > pre_diff: pre_diff = xxx, pre_val = xxx
return pre_val
时间复杂度：O(h)
空间复杂度：O(h)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def closestValue(root: TreeNode, target: float) -> int:
    pre_val = root.val
    pre_diff = abs(target - root.val)

    def dfs(root: TreeNode) -> int:
        nonlocal pre_diff
        nonlocal pre_val
        if root is None:
            return
        if abs(root.val - target) < pre_diff:
            pre_diff = abs(root.val - target)
            pre_val = root.val
        if root.val == target:
            return
        elif root.val > target:
            dfs(root.left)
        else:
            dfs(root.right)

    dfs(root)
    return pre_val
