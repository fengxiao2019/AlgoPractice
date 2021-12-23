# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
BFS 算法，能够得到的结果是：3, 9, 20, 15, 7
我们期望的结果是:[[3],[9, 20], [15, 7]]
如果我们知道当前处理的具体是哪一层，就容易得到结果了
方法1: 记录每个元素所属层，可以通过元组的方式记录，也可以用另一个队列记录高度
    [(3, 0)]   => [[3]]
    [(9, 1), (20, 1)] ->[[3], [9, 20]]
    [(15, 2), (7, 2)] -> [[3], [9, 20], [15, 7]]
方法2: 找规律，因为是逐层处理，所以我们可以不用记录第几层，主要逐层处理所有元素，然后把当前层的结果保存就可以了
例如：第0层：队列 [3]      结果集：[[3]]
     第1层：队列 [9, 20]  结果集：[[3], [9, 20]]
     第二层：队列 [15, 7] 结果集：[[3], [9, 20], [15, 7]]
"""
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
             return []
        queue = deque([(root, 0)])
        ans = []
        while queue:
            node, depth = queue.popleft()
            if depth >= len(ans):
                ans.append([node.val])
            else:
                ans[depth].append(node.val)
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        return ans


    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
             return []
        queue = deque([root])
        ans = []
        while queue:
            length = len(queue)
            cur_floor = []
            for i in range(length):
                top = queue.popleft()
                cur_floor.append(top.val)
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
            ans.append(cur_floor)
        return ans

"""
DFS 算法，先序遍历-能够得到的结果是：3, 9, 20, 15, 7
可以在遍历的过程中记录深度，得到的结果是[(3, 0), (9, 1), (20, 1), (15, 1), (7, 1)], 然后再一次遍历，生成结果集
"""
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        def dfs(root: TreeNode, depth: int) -> NoReturn:
            if root is None: return
            ans.append((root.val, depth))
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        dfs(root, 0)
        res = []
        for val, depth in ans:
            if depth >= len(res):
                res.append([val])
            else:
                res[depth].append(val)
        return res


"""
可以避免第二次的遍历吗？
可以在递归的过程中填充结果集
例如：套用先序遍历的模版
if root is None: return
# do something
dfs(root.left)
dfs(root.right)
我们可以在 ‘do something’中 完成逻辑
if len(ans) <= depth:
    ans.append([root.val])
else:
    ans[depth].append(root.val)
"""

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        def dfs(root: TreeNode, depth: int) -> NoReturn:
            if root is None: return
            if depth >= len(ans):
                ans.append([root.val])
            else:
                ans[depth].append(root.val)
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        dfs(root, 0)
        return ans
