# %%
# l-> left; r: right; n: node
# the position of n indicate the search method.
# eg: `lnr`, the position of n is in the middle of the 
# string 'lnr', so the search method is 'in porder'
# so: 
# lnr = in order
# lrn = post order
# nlr = pre order
import inspect
import random
import sys
from collections import defaultdict
INT_MIN = -sys.maxsize - 1


class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __repr__(self):
        return f"<Node>: {self.key}"


class NodeList(object):
    def __init__(self, key):
        assert key is not None, "key cannot be None"
        self.head = Node(key)

    def insert(self, key):
        """insert traversal"""
        root = self.head
        new_leaf = Node(key)
        while root:
            if root.key > key:
                if root.left:
                    root = root.left
                else:
                    root.left = new_leaf
                    break
            elif root.key < key:
                if root.right:
                    root = root.right
                else:
                    root.right = new_leaf
                    break
                
    @classmethod
    def _insert(cls, node, key):
        if node.key >= key:
            if not node.left:
                node.left = Node(key)
            else:
                cls._insert(node.left, key) 
        else:
            if not node.right:
                node.right = Node(key)
            else:
                cls._insert(node.right, key)

    def insert_decursive(self, key):
        self._insert(self.head, key)

    @classmethod
    def _search_nlr(cls, node, key):
        """ pre order """
        if node is None or node.key == key:
            print(f"find key: {node}")
            return node
        print(f"search_left: {node}.left:{node.left}")
        res = cls._search_nlr(node.left, key)
        if res:
            print(f"出栈:{node}")
            return res
        print(f"search_right: {node}.right:{node.right}")
        res = cls._search_nlr(node.right, key)
        return res

    def search_nlr_traversal(self, key):
        tmp_stack = [self.head]
        while tmp_stack:
            node = tmp_stack.pop()
            if node.key == key:
                return node
            # FIFO, first left then right,
            # so we insert right first then the left node
            if node.right:
                tmp_stack.append(node.right)
            if node.left:
                tmp_stack.append(node.left)
        print(tmp_stack)
        return None

    @classmethod
    def _search_lnr(cls, node, key):
        frame_id = id(inspect.currentframe())
        print(f"frame_id: {frame_id}")
        if node is None:
            return node

        print(f"search_left: {node}.left:{node.left}")
        res = cls._search_lnr(node.left, key)
        if res:
            print(f"出栈时机-左节点发现结果: {node} frame_id:{frame_id}")
            return res
        if node.key == key:
            return node
        print(f"search_right: {node}.right:{node.right}")
        res = cls._search_lnr(node.right, key)
        if res:
            print(f"出栈时机-左节点发现结果: {node} frame_id:{frame_id}")
        return res

    def search_lnr_traversal(self, key):
        tmp_stack = []
        node = self.head
        while tmp_stack or node is not None:
            if node is not None:
                tmp_stack.append(node)
                node = node.left
            else:
                node = tmp_stack.pop()
                if node.key == key:
                    return node
                node = node.right

    @classmethod
    def _search_lrn(self, node, key):
        frame_id = id(inspect.currentframe())
        print(f"frame_id: {frame_id}")
        if node is None:
            return node
        print(f"search_right: {node}.right:{node.right}")
        res = self._search_lrn(node.right, key)
        if res:
            print(f"出栈时机-左节点发现结果: {node} frame_id:{frame_id}")
            return res
        print(f"search_left: {node}.left:{node.left}")
        res = self._search_lrn(node.left, key)
        if res:
            print(f"出栈时机-右节点发现结果: {node} frame_id:{frame_id}")
            return res
        if node.key == key:
            return node

    def search_lrn_traversal(self, key):
        """
        非递归方式, 特点是压栈再按顺序出栈
        """
        tmp_stack = []
        node = self.head
        last_visited_node = None
        while tmp_stack or node is not None:
            if node is not None:
                tmp_stack.append(node)
                node = node.left
            else:
                # if left node is None, get the right node
                # first retrive the peek node of stack, 
                # this node is the parent node
                peek_node = tmp_stack[-1]
                # if you don't add the last condition, the loop will be infinite
                # because the peek_node always the last index of tmp_stack
                if peek_node.right and last_visited_node != peek_node.right:
                    node = peek_node.right
                else:
                    if peek_node.key == key:
                        return peek_node
                    last_visited_node = tmp_stack.pop()
        return None

    def search(self, key) -> Node:
        # import ipdb; ipdb.set_trace()
        self._search_nlr(self.head, key)
        print("\n\n\n")
        self._search_lnr(self.head, key)
        print("\n\n\n")
        return self._search_lrn(self.head, key)

    def print_tree(self, root, indent, last):
        if not root:
            return
        print(indent, end='')
        if last:
            print("\\--", end=' ')
            indent += "  "
        else:
            print("|--", end=' ')
            indent += "| "
        print(f"{root.key}")
        self.print_tree(root.left, indent, False)
        self.print_tree(root.right, indent, True)

    def bfs_search(self, key):
        tmp_dequeue = [self.head]
        while tmp_dequeue:
            # 注意这里要用pop(0)
            node = tmp_dequeue.pop(0)
            if node.key == key:
                return node
            if node.left:
                tmp_dequeue.append(node.left)
            if node.right:
                tmp_dequeue.append(node.right)

    def bfs(self):
        "按层级打印"
        tmp_dequeue = [self.head]
        level_nodes = 0
        while tmp_dequeue:
            level_nodes = len(tmp_dequeue)
            print(tmp_dequeue)
            while level_nodes > 0:
                # 注意这里是pop(0)，按照FIFO的方式弹出数据
                node = tmp_dequeue.pop(0)
                print(f"{node.key}", end=' ')
                if node.left:
                    tmp_dequeue.append(node.left)
                if node.right:
                    tmp_dequeue.append(node.right)
                level_nodes -= 1
            print('')
        print("")

    def bfs_normal(self):
        print("begin to bfs normal")
        level_nodes = self._level_nodes()
        for item in level_nodes:
            print(item)
        print("end \n")
    
    def bfs_reverse(self):
        print("begin to bfs reverse")
        level_nodes = self._level_nodes()
        for item in level_nodes[::-1]:
            print(item)
        print("end \n")

    def bfs_z_shape(self):
        print("begin to z shape bfs")
        level_nodes = self._level_nodes()
        for index, item in enumerate(level_nodes):
            if index % 2 != 0:
                print(item[::-1])
            else:
                print(item)
        print("end \n")

    def _level_nodes(self):
        """从最底层向上打印"""
        tmp_dequeue = [self.head]
        level_nodes = []
        level_node_count = 0

        while tmp_dequeue:
            level_nodes.append(list(tmp_dequeue))
            level_node_count = len(tmp_dequeue)
            while level_node_count > 0:
                node = tmp_dequeue.pop(0)
                if node.left:
                    tmp_dequeue.append(node.left)
                if node.right:
                    tmp_dequeue.append(node.right)
                level_node_count -= 1
        return level_nodes

    def bfs_reverse(self):
        """从最底层向上打印"""
        tmp_dequeue = [self.head]
        level_nodes = []
        level_node_count = 0

        while tmp_dequeue:
            level_nodes.append(list(tmp_dequeue))
            level_node_count = len(tmp_dequeue)
            while level_node_count > 0:
                node = tmp_dequeue.pop(0)
                if node.left:
                    tmp_dequeue.append(node.left)
                if node.right:
                    tmp_dequeue.append(node.right)
                level_node_count -= 1
        print("begin to print reverse bfs")
        for item in level_nodes[::-1]:
            print(item)
        print("reverse bfs end")

    def get_depth(self, node, key, height):
        """获取某个节点的"""
        if node is None:
            return 0
        if node.key == key:
            return height

        left = self.get_depth(node.left, key, height + 1)
        right = self.get_depth(node.right, key, height + 1)
        return max(left, right)

    def get_max_depth(self, node):
        """获取二叉树最大深度"""
        if node is None:
            return 0
        left = self.get_max_depth(node.left)
        right = self.get_max_depth(node.right)
        return max(left, right) + 1
       
    def get_lca(self, root, p, q):
        """get lowest common ancestor"""
        if root is None:
            return root
        if root.key == p or root.key == q:
            return root
        left = self.get_lca(root.left, p, q)
        right = self.get_lca(root.right, p, q)
        if left is None:
            return right
        if right is None:
            return left
        return root

    def divide_and_conquer_lrn(self, root):
        """通过分治法遍历二叉树 post-order"""
        result = []
        if root is None:
            return result
        left = self.divide_and_conquer_lrn(root.left)
        right = self.divide_and_conquer_lrn(root.right)
        result.extend(left)
        result.extend(right)
        result.append(root)
        return result

    def traversal_lrn(self):
        """遍历形式的post-order"""
        node = self.head
        results = []

        last_visited_node = None
        while results or node is not None:
            if node is not None:
                results.append(node)
                node = node.left
            else:
                peek = results[-1]
                if peek.right and last_visited_node != peek.right:
                    node = peek.right
                else:
                    print(peek)
                    last_visited_node = results.pop()

    def traversal_lnr(self):
        """遍历形式的 mid-order"""
        tmp_result = []
        node = self.head
        while tmp_result or node:
            if node is not None:
                tmp_result.append(node)
                node = node.left
            else:
                node = tmp_result.pop()
                print(node)
                node = node.right

    def traversal_nlr(self):
        """遍历形式的pre-order"""
        tmp_result = [self.head]
        while tmp_result:
            node = tmp_result.pop()
            print(node)
            if node.left:
                tmp_result.append(node.left)
            if node.right:
                tmp_result.append(node.right)

    def divide_and_conquer_lnr(self, root):
        """通过分治法遍历二叉树 mid-order"""
        reslut = []
        if root is None:
            return []
        left = self.divide_and_conquer_lnr(root.left)
        right = self.divide_and_conquer_lnr(root.right)
        reslut.extend(left)
        reslut.append(root)
        reslut.extend(right)
        return reslut

    def divide_and_conquer_nlr(self, root):
        """通过分治法遍历二叉树 pre-order"""
        reslut = []
        if root is None:
            return []
        left = self.divide_and_conquer_lnr(root.left)
        right = self.divide_and_conquer_lnr(root.right)
        reslut.append(root)
        reslut.extend(left)
        reslut.extend(right)
        return reslut

    def balance(self):
        balanced, _ = self.max_depth(self.head)
        return balanced
    
    def max_depth(self, root):
        if root is None:
            return True, 0
        l_balanced, left = self.max_depth(root.left)
        r_balanced, right = self.max_depth(root.right)
        balanced = l_balanced and r_balanced and abs(right - left) <= 1
        height = max(right, left) + 1
        return balanced, height
    
    def max_path_sum(self):
        result = self._helper(self.head)
        return result[1]


max_path_sum_res = INT_MIN


def _helper(self, root):
    """
             17
           /  \
          13  -29
          /    /  \
        -15   -14  15
        / \    / \
       9  -7  0   14

    9-> [9, 9]
    -7-> [-7, -7]
    -15 -> [-6, 9]
    13 -> [13, 9]
    """
    nonlocal  max_path_sum_res
    if root is None:
        return INT_MIN
    left = self._helper(root.left)
    right = self._helper(root.right)
    single_path_max = max(max(left, right) + root.key, root.key)
    max_top = max(single_path_max, left + right + root.key)
    max_path_sum_res = max(max_path_sum_res, max_top)


def test_insert1():
    print("\nbegin to test_insert1")

    tree = NodeList(numbers[0])
    print(numbers)
    for i in numbers[1:]:
        tree.insert_decursive(i)
    tree.bfs()
    tree.bfs_normal()
    tree.bfs_z_shape()
    tree.bfs_reverse()
    tree.print_tree(tree.head, "", False)
    # # pre-order
    # search_res = tree.search_nlr_traversal(8)
    # assert search_res.key == 8
    # # post-order
    # search_res = tree.search_lrn_traversal(9)
    # assert search_res.key == 9
    # # # in-order
    # search_res = tree.search_lnr_traversal(5)
    # assert search_res.key == 5
    # # breadth-fist-search
    # search_res = tree.bfs_search(5)
    # assert search_res.key == 5
    
    # if search_res:
    #     print(f"search result: {search_res}, left: {search_res.left}, right: {search_res.right}")
    # else:
    #     print(f"search result: {search_res}")
    print(f"p: {numbers[6]}, q: {numbers[12]}")
    res = tree.get_lca(tree.head, numbers[6], numbers[12])
    print(f"lca : {res}")
    depth_dict = defaultdict(list)
    for item in numbers:
        de = tree.get_depth(tree.head, item, 0)
        depth_dict[de].append(item)
    print(depth_dict)
    print(f"max_depth: {tree.get_max_depth(tree.head)}")
    result = tree.divide_and_conquer_lrn(tree.head)
    print(result)
    result = tree.divide_and_conquer_nlr(tree.head)
    print(result)
    result = tree.divide_and_conquer_lnr(tree.head)
    print(result)
    print("begin to traversal:lrn")
    tree.traversal_lrn()
    print("begin to traversal: lnr")
    tree.traversal_lnr()
    print("begin to traversal: nlr")
    tree.traversal_nlr()
    balanced = tree.balance()
    if balanced:
        print("平衡")
    else:
        print("不平衡")


def test_insert2():
    print("\nbegin to test_insert2")
    tree = NodeList(0)
    for i in [1, 12, 8, 9, 3, 5]:
        tree.insert(i)
    tree.print_tree(tree.head)


numbers = random.sample(range(200), 20)
test_insert1()
test_insert2()