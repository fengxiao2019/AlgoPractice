import unittest
import importlib
perm_module = importlib.import_module('daily.20210504.permutations')


class TestParentThesis(unittest.TestCase):
    def test_1(self):
        self.assertEqual(perm_module.generate_parentheses(1), ['()'])

    def test_2(self):
        self.assertEqual(perm_module.generate_parentheses(2), ['(())', '()()'])
