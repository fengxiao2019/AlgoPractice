
"""
二叉树节点
"""
from functools import wraps
from typing import List


def none_decorator(fun):
    @wraps(fun)
    def wraper(self, *args, **kwargs):
        if self.head is None:
            self.head = TreeNode(*args, **kwargs)
        return fun(self, *args, **kwargs)
    return wraper


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return f"<Node> {self.val}"


class MorrisMixin(object):
    """
    遍历步骤：
    step1: 初始化根为当前节点curr。

    step2: 当curr不是NULL时，检查curr是否有一个左边的孩子。

    step3: 如果curr没有左边的子节点，打印curr并将其更新为指向curr右边的节点。

    step4: 否则，使curr成为curr的左子树中最右边的节点的右子。

    step5: 将curr更新到这个左节点。
    时间复杂度：O(n)
    空间复杂度：O(1)
    """

    def inorder(self):
        res = []
        root = self.head
        prev = None
        while root:
            if root.left is None: # 如果左节点为空
                res.append(root.val)  # 可以把当前值存储
                root = root.right # 进入右节点
            else:
                # 找前驱节点
                prev = root.left
                while prev.right and prev.right != root:
                    prev = prev.right

                # 如果是正常结束的
                if prev.right is None:
                    prev.right = None
                    root = root.left
                else:
                    res.append(root.val)
                    prev.right = None
                    root = root.right
            return res

    def preorder(self):
        """
        先处理当前节点
        如果当前节点不存在左子树，
        :return:
        """
        res = []
        root = self.head
        pre = None
        while root:
            res.append(root.val)
            if not root.left:
                root = root.right
            else:
                pre = root.left
                while pre.right: pre = pre.right
                # 将后继节点指向当前节点的右子树
                pre.right = root.right
                root.right = None

                root = root.left
        return res

    def postorder(self):
        res = []
        dummy = TreeNode('dummy')
        dummy.left = self.head
        root = dummy
        prev = None
        while root:
            # 左子树不存在，进入右子树处理
            if root.left is None:
                root = root.right
            else:
                # 左子树存在，进入左子树
                prev = root.left
                # 找前驱节点
                while prev.right and prev.right != root:
                    prev = prev.right
                # 如果前驱节点自然结束
                if prev.right is None:
                    # 将前驱节点指向后继节点
                    # 处理左节点
                    prev.right = root
                    root = root.left
                else:
                    # 在这里处理后序访问
                    self._visit_reverse(root.left, prev, res)
                    prev.right = None  # 断开 前驱节点到后继节点的连接
                    # 前驱节点处理完了，恢复树
                    root = root.right
            print(prev, root)

    def _reverse(self, node1: TreeNode, node2: TreeNode) -> (TreeNode, TreeNode):
        print(node1.val, node2.val)
        prev = node1
        head = prev.right

        if node1 == node2:
            return (node1, node2)

        prev.right = None

        while head != node2:
            print(head.val)
            tmp = head.right
            head.right = prev
            prev = head
            head = tmp
        return prev, node1

    def _visit_reverse(self, node1: TreeNode, node2: TreeNode, res: List[int]) -> None:
        print(res)
        print(node1, node2)
        start, end = self._reverse(node1, node2)
        node = start
        while node != end:
            res.append(node.val)
            node = node.right
        res.append(node2.val)
        self._reverse(end, start)


class RecursiveMixin(object):
    def inorder(self):
        res = []
        print("enter recursive inorder")
        def helper(root: TreeNode) -> None:
            if root is None: return
            helper(root.left)
            res.append(root.val)
            helper(root.right)

        helper(self.head)
        return res

    def preorder(self):
        res = []

        def helper(root: TreeNode) -> None:
            if root is None: return
            res.append(root.val)
            helper(root.left)
            helper(root.right)
        helper(self.head)
        return res

    def postorder(self):
        res = []

        def helper(root: TreeNode) -> None:
            if root is None: return
            helper(root.left)
            helper(root.right)
            res.append(root.val)
        helper(self.head)
        return res


class NonRecursiveMixin(object):
    def inorder(self):
        stack = []
        res = []
        root = self.head
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                peek = stack.pop()
                res.append(peek.val)
                root = peek.right
        return res

    def preorder(self):
        stack = [self.head]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

    def postorder(self):
        stack = []
        res = []
        root = self.head
        last_visited = None
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                peek = stack[-1]
                if peek.right and peek.right != last_visited:
                    root = peek.right
                else:
                    last_visited = stack.pop()
                    res.append(last_visited.val)
        return res


class BSTBase(object):
    def __init__(self, val=None):
        self.head = None if val is None else TreeNode(val)

    @none_decorator
    def insert(self, val: int) -> None:
        """
        二叉搜索树插入元素
        :param val: 待插入的值
        :return: None
        时间复杂度：O(h)
        """
        node = TreeNode(val)
        root = self.head
        while True:
            if root.val == val:
                return
            elif root.val > node.val:
                if root.left:
                    root = root.left
                else:
                    root.left = node
                    return
            else:
                if root.right:
                    root = root.right
                else:
                    root.right = node
                    return

    @none_decorator
    def insert_recursive(self, val: int) -> None:
        root = self.head

        def insert_help(root: TreeNode, val: int) -> TreeNode:
            """
            :param root: 待插入的节点
            :param key:
            :return:
            """
            if root is None:
                root = TreeNode(val)
            elif val < root.val:
                root.left = insert_help(root.left, val)
            else:
                root.right = insert_help(root.right, val)
            return root
        return insert_help(root, val)

    @property
    def min(self) -> int:
        root = self.head
        if root:
            while root.left:
                root = root.left
        return root.val

    @property
    def max(self) -> int:
        root = self.head
        if root:
            while root.right:
                root = root.right
        return root.val

    @staticmethod
    def _predecessor(root: TreeNode) -> int:
        # 左子树的最右节点
        root = root.left
        while root.right:
            root = root.right
        return root.val

    @staticmethod
    def _successor(root: TreeNode) -> int:
        # 右子树的最左节点
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def delete(self, root: TreeNode, val: int) -> TreeNode:
        """
        删除节点
        case 1: 叶子节点-> root = None
        case 2: 删除的节点存在左节点 -> 用节点中的最大值替换
        case 3： 删除的节点存在右节点 -> 用节点中最小值替换
        """
        if not root:
            return None
        if val > root.val:
            root.right = self.delete(root.right, val)
        elif val < root.val:
            root.left = self.delete(root.left, val)
        else:
            # 是叶子节点
            if root.left is None and root.right is None:
                root = None
            elif root.right:
                root.val = self._successor(root)
                root.right = self.delete(root.right, root.val)
            else:
                root.val = self._predecessor(root)
                root.left = self.delete(root.left, root.val)
        return root
    
    def del_min(self) -> None:
        self.delete(self.head, self.min)

    def del_max(self) -> None:
        self.delete(self.head, self.max)

    def search(self, val: int) -> TreeNode:
        root = self.head
        while root:
            if root.val == val:
                break
            elif root.val > val:
                root = root.left
            else:
                root = root.right
        return root

    def search_recursive(self, root: TreeNode, val: int) -> TreeNode:
        if root is None: return None
        if root.val > val:
            return self.search_recursive(root.left, val)
        elif root.val < val:
            return self.search_recursive(root.right, val)
        else:
            return root

    @staticmethod
    def find_kth(root: TreeNode, k: int) -> TreeNode:
        """
        中序遍历返回的就是第k小的数据，可以利用中序遍历实现
        """
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                peek = stack.pop()
                k -= 1
                if k == 0:
                    return peek.val
                if peek.right:
                    root = peek.right

    def ceil(self, val: int) -> int:
        """
        大于等于val并且node.val - val 差最小

        解题思路：node.val > val:
                    node.left is None: node
                    node.left < val: node

                  8
                /   \
              4      12
            /  \    /  \
           2    6  10   14

        Key: 11  Floor: 10  Ceil: 12
        Key: 1   Floor: -1  Ceil: 2
        Key: 6   Floor: 6   Ceil: 6
        Key: 15  Floor: 14  Ceil: -1
        """
        root = self.head
        pre = -1
        while root:
            if root.val > val:
                pre = root.val
                root = root.left
            elif root.val < val:
                root = root.right
            else:
                pre = root.val
                break
        return pre

    def floor(self, val: int) -> int:
        root = self.head
        pre = -1
        while root:
            if root.val == val:
                pre = root.val
                break
            elif root.val > val:
                root = root.left
            elif root.val < val:
                pre = root.val
                root = root.right
        return pre

    def search_range(self, k1, k2):
        """
        Print BST keys in the given range
        Given two values k1 and k2 (where k1 < k2) and a root pointer to a Binary Search Tree.
        Print all the keys of the tree in range k1 to k2. i.e.
        print all x such that k1<=x<=k2 and x is a key of given BST.
        Print all the keys in increasing order.

                 20
                /   \
              8      22
            /  \
           4   12
        Input: k1 = 10 and k2 = 22
        Output: 12, 20 and 22.
        Explanation: The keys are 4, 8, 12, 20, and 22.
        So keys in range 10 to 22 is 12, 20 and 22.

        Input: k1 = 1 and k2 = 10
        Output: 4 and 8
        Explanation: The keys are 4, 8, 12, 20, and 22.
        So keys in range 1 to 10 is 4 and 8
        """
        # in-order traverse tmp_stack pop check the value is in the range or not
        stack = []
        root = self.head
        res = []
        while stack or root:
            if node:
                stack.append(node)
                node = node.left
            else:
                peek = stack.pop()
                if k1 < peek.val < k2:
                    res.append(peek.val)
                elif peek.key > k2:
                    break
                node = node.right
        return res

    def subtrees_count(self, k1, k2):
        """
                Input:
                10
              /    \
            5       50
           /       /  \
         1       40   100
        Range: [5, 45]
        Output:  1
        There is only 1 node whose subtree is in the given range.
        The node is 40

        Input:
                10
              /    \
            5       50
           /       /  \
         1       40   100
        Range: [1, 45]
        Output:  3
        There are three nodes whose subtree is in the given range.
        The nodes are 1, 5 and 40
        大问题划分成较小的问题
        假设要判断子树M是否满足条件，只需要子树M满足以下几个节点：
            1. 子树M的根节点root 满足条件
            2. 子树M的左子树满足条件
            3. 子树M的右子树满足条件
        >> 寻找base case
        base case: 叶子节点只需要叶子节点自身满足条件即可
        """

        def subtree_count_helper(root, k1, k2) -> (bool, int):
            if root is None:
                return True, 0

            left, count_l = subtree_count_helper(root.left, k1, k2)
            right, count_r = subtree_count_helper(root.right, k1, k2)

            if left and right and k1 <= root.val <= k2:
                return True, count_l + count_r + 1
            else:
                return False, count_l + count_r

        _, count = subtree_count_helper(self.root, k1, k2)
        return count

    def remove_all_leaf_nodes(self) -> None:
        """
        原理很简单，大问题化成小问题，删除以节点f为根节点的树等价于 ：
        1. 删除f的左子树的叶子节点
        2. 删除f的右子树的叶子节点
        specical case: 1. 根节点为空 2. 根节点即叶子节点
        base case： 叶子节点，删除即可
        """

        def remove_leave(parent: TreeNode, node: TreeNode) -> None:
            if node.left is None and node.right is None:
                if parent.key > node.key:
                    parent.left = None
                else:
                    parent.right = None
            if node.left:
                remove_leave(node, node.left)
            if node.right:
                remove_leave(node, node.right)

        # 根结点是空节点
        if not self.head:
            return
        # 根结点是叶子节点
        if self.head and self.head.left is None and self.head.right is None:
            # 根节点即叶子节点
            self.head = None
            return

        if self.head and self.head.left:
            remove_leave(self.head, self.head.left)
        if self.root and self.head.right:
            remove_leave(self.head, self.head.right)

    def sum_k_smallest_elements(self, k: int) -> int:
        # Sum of k smallest elements in BST
        # BST的特性：中序遍历即排序
        # 所以利用traverse遍历，累加前k个元素就可以
        stack = []
        node = self.head
        count = 0
        sum_v = 0
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                peek = stack.pop()
                count += 1
                if count <= k:
                    sum_v += peek.key
                else:
                    break
        return sum_v

    @staticmethod
    def successor(root: TreeNode, val: int) -> TreeNode:
        node = None

        def helper(root: TreeNode, val: int) -> int:
            if root is None:
                return None
            nonlocal node
            if root.val > val:
                node = root
                helper(root.left, val)
            else:
                helper(root.right, val)
            return node.val if node else None
        return helper(root, val)

    @staticmethod
    def predecessor(root: TreeNode, val: int) -> TreeNode:
        node = None

        def helper(root: TreeNode, val: int):
            if root is None:
                return None
            nonlocal node
            if root.val < val:
                node = root
                helper(root.right, val)
            else:
                helper(root.left, val)
            return node.val if node else None
        return helper(root, val)


class BSTMorris(BSTBase, MorrisMixin):
    pass


class BSTNonRecursive(BSTBase, NonRecursiveMixin):
    pass


class BSTRecusive(BSTBase, RecursiveMixin):
    pass


class BinaryTree(object):
    def __init__(self):
        self.head = None

    def insert(self):
        pass

    def to_bst(self):
        pass


if __name__ == '__main__':
    print(BSTMorris.__mro__)