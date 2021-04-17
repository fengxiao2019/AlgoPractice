"""
剑指 Offer 07. 重建二叉树
思路：preorder 确定root 节点
preorder = [root 左子树   右子树]
inorder = [左子树 root 右子树]
从preorder 和 inorder的结构中可以看出，
重构以root的为节点的树，可以划分成：
1. 重构以root.left为节点的左子树 和 以root.right 为节点的右子树
2. 这可以使用递归思路实现

test case:
1. len(preorder) != len(inorder) or not preorder:
    return None

2. 单节点，返回 root

3. 只有左子树
4. 只有右子树
5. common case
递归函数：用index 确定左右子树边界
时间复杂度：O(n)
空间复杂度：O(h)
"""
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder: List[int], inorder: List[int]) -> TreeNode:
    # 处理边界条件
    if len(preorder) != len(inorder) or not preorder:
        return None

    # 遍历inorder map node.val 和 index
    in_map = {item: i for i, item in enumerate(inorder)}

    # 递归函数
    def dfs(p_s: int, p_e: int, in_s: int, in_e: int) -> TreeNode:
        # 处理递归出口
        if p_s > p_e:
            return None
        # 构造root 节点
        root_val = preorder[p_s]
        root_i = in_map[root_val]

        root_node = TreeNode(root_val)
        pre_len = root_i - in_s
        # 构造左子树
        root_node.left = dfs(p_s + 1, p_s + pre_len, in_s, root_i - 1)
        # 构造右子树
        root_node.right = dfs(p_s + pre_len + 1, p_e, root_i + 1, in_e)
        return root_node

    return dfs(0, len(preorder) - 1, 0, len(inorder) - 1)