# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        res = tree_double_list(root)
        print(res)
        return res


"""
解题思路
中序遍历返回的是排序的结果
可以在返回中序遍历的过程中构造双向循环链表
时间复杂度：O(n) 遍历了所有节点
空间复杂度：O(1)
"""


def tree_double_list(root: 'None') -> 'Node':
    if not root:
        return
    dummy = Node('dummy')
    head = dummy

    def inorder(head, root: 'Node') -> 'Node':
        stored_head = head
        stack = []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                #
                cur = stack.pop()
                head.right = cur
                cur.left = head
                head = cur
                if cur.right:
                    node = cur.right

        head.right = stored_head.right
        stored_head.right.left = head

    inorder(head, root)
    return dummy.right