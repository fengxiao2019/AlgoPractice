# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if root is None:
            return False
        return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)


"""
解题思路：
思路和检查是否子树的思路一样
采用深度优先的方式，单独检查每一条路径

if head is None: return True
if root is None: return False 
if root.val != head.val:
      return False
else:
    检查head.next, root.left 或者 head.next, root.right 有一个满足就行

这里容易出现问题的地方在这里：

if root.val != head.val:
    return dfs(head, root.left) or dfs(head, root.right)
这个逻辑表面上看上去是正确的，但是因为会导致link 不连续存在于树中，造成存在的假象
必须要保证当前节点是相等的，才能继续执行。

时间复杂度：O(n) 最差情况下，二叉树本身就是一个链表，head 也是一个链表，而且链表存在于二叉树中
空间复杂度：O(n) 递归的深度为二叉树的深度
"""


def dfs(head: ListNode, root: TreeNode):
    if head is None: return True
    if root is None: return False

    if root.val != head.val:
        return False
    else:
        return dfs(head.next, root.left) or dfs(head.next, root.right)
    return dfs(head, root)
