import unittest
# import importlib
# perm_module = importlib.import_module('daily.20210504.permutations')
import daily.L20210504.permutations as perm_module


class TestParentThesis(unittest.TestCase):
    def test_1(self):
        self.assertEqual(perm_module.generate_parentheses(1), ['()'])

    def test_2(self):
        self.assertEqual(perm_module.generate_parentheses(2), ['(())', '()()'])

    def test_valid_False(self):
        self.assertFalse(perm_module.valid('('))
        self.assertFalse(perm_module.valid(')'))
        self.assertFalse(perm_module.valid('))'))
        self.assertFalse(perm_module.valid('())'))

    def test_valid_True(self):
        self.assertTrue(perm_module.valid('()'))
        self.assertTrue(perm_module.valid('(())'))
        self.assertTrue(perm_module.valid('((()))'))
        self.assertTrue(perm_module.valid('()()()'))


class TestPermutations(unittest.TestCase):
    def test_1(self):
        self.assertEqual(perm_module.permutations([1]), [[1]])

    def test_2(self):
        self.assertEqual(perm_module.permutations([1, 2]), [[1, 2], [2, 1]])

