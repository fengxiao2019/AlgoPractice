from DataStructure.cache.lru import LRUCache
import unittest

from functools import lru_cache
class TestLRUCache(unittest.TestCase):
    def test_get(self):
        instance = LRUCache(2)
        instance[3] = 3
        instance[4] = 4
        instance.get(4)
        instance.put(5, 5)