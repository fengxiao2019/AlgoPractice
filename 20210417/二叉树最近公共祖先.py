"""
解题思路：
分别在左子树 和 右子树中查找p 或者 q
    case 1: 查到 -> 返回查到的节点
    case 2: 没查到 -> 继续查左右子节点

    退出条件
    left and right: return root
    if left: return left
    if right: return right

test case:
# 边界case
None 节点 -> return None
时间复杂度：
空间复杂度：
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root:
        return None

    if root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    if left: return left
    if right: return right
    return None


"""
解题思路：
从子树朝上找
遍历这颗树，存储子节点和父节点的对应关系
分别从p 和 q 同时 沿着父节点找，找到第一个相遇的节点，就是第一个公共父节点
时间复杂度：O(n)
空间复杂度：O(n)
"""


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # 边界条件处理
    if not root: return None

    # 构造子树 -> 父亲树的映射关系
    node_map = {root: None}

    def dfs(root: TreeNode):
        if root.left:
            node_map[root.left] = root
            dfs(root.left)
        if root.right:
            node_map[root.right] = root
            dfs(root.right)

    dfs(root)
    # 记录已经访问的节点
    map_v = set()
    while p:
        map_v.add(p)
        p = node_map[p]

    while q:
        if q in map_v:
            return q
        else:
            q = node_map[q]
    return None