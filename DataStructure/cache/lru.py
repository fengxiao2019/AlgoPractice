from collections import OrderedDict
from dataclasses import dataclass


from functools import lru_cache

class LRUCache(OrderedDict):
    """
    基于OrderedDict实现
    'Limit size, evicting the least recently looked-up key when full'
    """

    def __init__(self, capacity=128, *args, **kwds):
        self.capacity = capacity
        super().__init__(*args, **kwds)

    def __getitem__(self, key):
        value = super().__getitem__(key)
        self.move_to_end(key)
        return value

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        if len(self) > self.capacity:
            oldest = next(iter(self))  # 获取第一个值

            del self[oldest]

    def put(self, key: int, value: int) -> int:
        self[key] = value

    def get(self, key: int) -> int:
        if key in self:
            return self[key]
        return -1


class LRU_V2(object):
    def __int__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


@dataclass
class _Node(object):
    __slots__ = 'count', 'val'

    count: int
    val: 'typing.Any'
    key: 'typing.Any'
