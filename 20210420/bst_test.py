import unittest
from binary_search_tree import BSTBase as BST, BSTMorris, \
    BSTNonRecursive, BSTRecusive, TreeNode
import random
from typing import List


def _construct(nums: List[int], bst_class) -> TreeNode:
    if not nums:
        return None
    bst_proxy = bst_class(nums[0])
    for item in nums:
        bst_proxy.insert(item)
    return bst_proxy

class Mixin(object):

    def tree_nlr(self, root: TreeNode) -> List[TreeNode]:
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val if node else 'null')
            if node:
                stack.append(node.right)
                stack.append(node.left)
        return res

    def tree_lnr(self, root: TreeNode) -> List[int]:
        stack = []
        node = root
        res = []
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                peek = stack.pop()
                res.append(peek.val)
                if peek.right:
                    node = peek.right
        return res

    @staticmethod
    def construct_tree(nums, bst_class=BST) -> BST:
        # 原则：从nums中每次选取最大的值作为root，
        # 左边的节点从左边的列表中选择最大值
        # 右边的节点从右边的列表中选择最大的值
        return _construct(nums, bst_class)


class BstTestCase(unittest.TestCase, Mixin):
    def setUp(self) -> None:

        self.root = BST(12)
        self.empty_root = BST()
        self.sample = random.sample(range(1000), k=5)

    def test_None(self):
        self.empty_root.insert(12)
        self.assertEqual(self.empty_root.head.val, 12)

    def test_exists(self):
        self.root.insert(12)
        self.assertEqual(self.tree_nlr(self.root.head), [12, 'null', 'null'])

    def test_None_recursive(self):
        self.empty_root.insert_recursive(12)
        self.assertEqual(self.empty_root.head.val, 12)

    def test_recursive_exists(self):
        self.empty_root.insert_recursive(12)
        self.empty_root.insert_recursive(12)
        self.assertEqual(self.tree_nlr(self.root.head), [12, 'null', 'null'])

    def test_construct(self):
        nums = random.sample(range(100), k=10)
        bst_proxy = self.construct_tree(nums)

        self.assertEqual(sorted(nums), self.tree_lnr(bst_proxy.head))

    def test_min(self):
        nums = random.sample(range(1000), k=10)
        bst_proxy = self.construct_tree(nums)
        print(nums, min(nums), bst_proxy.min)
        self.assertEqual(min(nums), bst_proxy.min)

    def test_max(self):
        nums = random.sample(range(1000), k=1)
        bst_proxy = self.construct_tree(nums)
        print(nums, max(nums), bst_proxy.max)
        self.assertEqual(max(nums), bst_proxy.max)

    def test_successor(self):
        nums = random.sample(range(1000), k=10)
        sorted_nums = sorted(nums)
        bst_proxy = self.construct_tree(nums)
        self.assertEqual(bst_proxy.successor(bst_proxy.head, 10000), None)
        self.assertEqual(bst_proxy.successor(bst_proxy.head, sorted_nums[4]),sorted_nums[5])

    def test_predecessor(self):
        nums = random.sample(range(1000), k=10)
        sorted_nums = sorted(nums)
        bst_proxy = self.construct_tree(nums)
        self.assertEqual(bst_proxy.predecessor(bst_proxy.head, 10000), sorted_nums[-1])
        self.assertEqual(bst_proxy.predecessor(bst_proxy.head, sorted_nums[4]),sorted_nums[3])

    def test_delete(self):
        nums = random.sample(range(1000), k=10)
        sorted_nums = sorted(nums)
        bst_proxy = self.construct_tree(nums)
        bst_proxy.delete(bst_proxy.head, sorted_nums[5])
        self.assertEqual(self.tree_lnr(bst_proxy.head), sorted_nums[:5] + sorted_nums[6:])

    def test_del_min(self):
        nums = random.sample(range(1000), k=10)
        sorted_nums = sorted(nums)
        bst_proxy = self.construct_tree(nums)
        bst_proxy.del_min()
        self.assertEqual(self.tree_lnr(bst_proxy.head), sorted_nums[1:])

    def test_del_min(self):
        nums = random.sample(range(1000), k=10)
        sorted_nums = sorted(nums)
        bst_proxy = self.construct_tree(nums)
        bst_proxy.del_max()
        self.assertEqual(self.tree_lnr(bst_proxy.head), sorted_nums[:-1])

    def test_search(self):
        bst_proxy = self.construct_tree(self.sample)
        self.assertEqual(bst_proxy.search(122214), None)
        self.assertEqual(bst_proxy.search(self.sample[-1]).val, self.sample[-1])
        self.assertEqual(bst_proxy.search(self.sample[0]).val, self.sample[0])
        self.assertEqual(bst_proxy.search(self.sample[5]).val, self.sample[5])

    def test_find_kth(self):
        bst_proxy = self.construct_tree(self.sample)
        sorted_sample = sorted(self.sample)
        self.assertEqual(bst_proxy.find_kth(bst_proxy.head, 4), sorted_sample[3])
        self.assertEqual(bst_proxy.find_kth(bst_proxy.head, 1), sorted_sample[0])
        self.assertEqual(bst_proxy.find_kth(bst_proxy.head, 3), sorted_sample[2])
        self.assertEqual(bst_proxy.find_kth(bst_proxy.head, len(self.sample)), sorted_sample[-1])
        self.assertEqual(bst_proxy.find_kth(bst_proxy.head, len(self.sample) + 1), None)

    def test_ceil(self):
        bst_proxy = self.construct_tree(self.sample)
        print(self.sample)
        self.assertEqual(bst_proxy.ceil(self.sample[5] - 1), self.sample[5])

    def test_floor(self):
        bst_proxy = self.construct_tree(self.sample)
        self.assertEqual(self.sample[5], bst_proxy.floor(self.sample[5] + 1))

    def test_inorder_recursive(self):
        bst_proxy = self.construct_tree(self.sample, BSTRecusive)
        sorted_sample = sorted(self.sample)
        self.assertEqual(bst_proxy.inorder(), sorted_sample)

    def test_inorder_Morris(self):
        bst_proxy = self.construct_tree(self.sample, BSTMorris)
        sorted_sample = sorted(self.sample)
        self.assertEqual(bst_proxy.inorder(), sorted_sample)

    def test_preorder(self):
        sample = self.sample
        morris = self.construct_tree(sample, BSTMorris)
        recursive = self.construct_tree(sample, BSTRecusive)
        nonrecursive = self.construct_tree(sample, BSTNonRecursive)
        self.assertEqual(morris.preorder(), recursive.preorder())
        self.assertEqual(morris.preorder(), nonrecursive.preorder())

    def test_postorder(self):
        sample = self.sample
        sample = [55, 82, 549, 44, 39]
        print(sample)

        morris = self.construct_tree(sample, BSTMorris)
        print(morris.preorder())
        res = morris.postorder()
        self.assertTrue(res, True)



if __name__ == '__main__':
    unittest.main()
