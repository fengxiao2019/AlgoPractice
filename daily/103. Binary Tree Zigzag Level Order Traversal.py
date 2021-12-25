# Definition for a binary tree node.
from typing import List
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        return zigzagLevelOrder(root)


"""
解题思路：
    用广度优先算法处理
抽象：
    用队列存储(节点)
    队列        长度               输出
    [3]          1                 3
    [9, 20]      2               20, 9
    [15, 7]      2               15, 7
两个while 循环
while queue:
    length = len(queue)
    while length > 0:
        logic 
        # 在这里处理具体是否翻转的逻辑
边界条件检查：
    空节点：空
    单节点：[[root.val]]  # 满足抽象的处理逻辑，不用单独处理

时空复杂度：
    Time Complexity: O(n)
    Space Complexity: O(n)
"""


def zigzagLevelOrder(root: TreeNode) -> List[List[int]]:
    if not root: return []
    # 定义一个结果集
    ans = []

    queue = [root]
    # 定义一个变量用来控制深度
    depth = 0
    while queue:
        length = len(queue)
        tmp_arr = []
        while length > 0:
            peek = queue.pop(0)
            tmp_arr.append(peek.val)
            length -= 1

            # 继续往队列中添加元素
            if peek.left:
                queue.append(peek.left)
            if peek.right:
                queue.append(peek.right)

        # 确定是否要输出逆向tmp_arr
        if depth % 2 == 1:
            ans.append(tmp_arr[::-1])
        else:
            ans.append(tmp_arr)
        # 深度递增
        depth += 1
    return ans


"""
解题思路：
    用深度优先算法解
抽象： 
    用hash表存储结果，key 为深度，value为列表，用defaultdict(list)
    递归时，传递深度到下层节点，将节点加入到hash表对应的key中
    采用前序遍历的方式
    eg: 遍历到节点9时，hash[1].append(9)
        遍历到节点20: hash[1].append(20)
        遍历到节点15: hash[2].append(15)
        遍历到节点7: hash[2].append(7)
    最后按照深度递增的顺序输出结果集
    如果深度 % 2 == 1: 将这一层的数据逆序

边界条件检查：
    空节点： []
    单节点：[[root.val]]
时间复杂度：
    Time Complexity: O(n)
    Space Complexity: O(n)
"""


def zigzagLevelOrder(root: TreeNode) -> List[List[int]]:
    # 边界条件检查
    if root is None:
        return []
    # 定义一个hash 表存储结果集

    hash_table = defaultdict(list)

    def dfs(root: TreeNode, depth: int) -> None:
        if root is None: return
        hash_table[depth].append(root.val)
        dfs(root.left, depth + 1)
        dfs(root.right, depth + 1)

    # 调用dfs
    dfs(root, 0)

    ans = []
    i = 0
    while True:
        if i not in hash_table:
            break

        # 处理zigzag
        if i % 2 == 1:
            ans.append(hash_table[i][::-1])
        else:
            ans.append(hash_table[i])

        i += 1
    return ans
