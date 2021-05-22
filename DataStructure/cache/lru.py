from weakref import proxy as _proxy
from collections import OrderedDict
# 主要考虑一下，当你要设计一个lru时需要考虑什么
# 首先是一个缓存
# 缓存有容量
# 支持的操作，get put clear

from dataclasses import dataclass

# https://medium.com/@epicshane/a-python-implementation-of-lfu-least-frequently-used-cache-with-o-1-time-complexity-e16b34a3c49b
@dataclass
class _Node(object):
    __slots__ = 'count', 'val'

    count: int
    val: 'typing.Any'
    key: 'typing.Any'


class LFU(object):
    # hash map + double link list
    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            self.cache[key].count += 1
            return self.cache[key].val

    def put(self, key, value):
        # 怎么实现O(1) ??
        if key not in self.cache:
            self.cache[key] = _Node(1, value, key)
        else:
            self.cache[key].val += 1
        if len(self.cache) > self.capacity:
            node = min(self.cache.values())
            del self.cache[node.key]



lfu_obj = LFU(10)
lfu_obj.put(1, 'shao')
lfu_obj.put('z', 'shao1')

lfu_obj.get('z')

print(lfu_obj.cache)


class LRU(OrderedDict):
    'Limit size, evicting the least recently looked-up key when full'

    def __init__(self, maxsize=128, *args, **kwds):
        self.maxsize = maxsize
        super().__init__(*args, **kwds)

    def __getitem__(self, key):
        value = super().__getitem__(key)
        self.move_to_end(key)
        return value

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        if len(self) > self.maxsize:
            oldest = next(iter(self))
            del self[oldest]

class LRU(object):
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


class CacheNode(object):
    def __init__(self, key, value, freq_node, pre, nxt):
        self.key = key
        self.val = value
        self.freq_node = freq_node
        self.pre = pre
        self.nxt = nxt

    def free_me(self):
        if self.freq_node.cache_head == self.freq_node.cache_tail:
            self.freq_node.cache_head = self.freq_node.cache_tail = None
        elif self.freq_node.cache_head == self:
            self.nxt.pre = None
            self.freq_node.cache_head = self.nxt
        elif self.freq_node.cache_tail == self:
            self.pre.nxt = None
            self.freq_node.cache_tail = self.pre
        else:
            self.pre.nxt = self.nxt
            self.nxt.pre = self.pre

        self.pre = None
        self.nxt = None
        self.freq_node = None


class FreqNode(object):
    def __init__(self, freq, pre, nxt):
        self.freq = freq
        self.pre = pre
        self.nxt = nxt
        self.cache_head = None
        self.cache_tail = None

    def count_cache(self):
        if self.cache_head is None and self.cache_tail is None:
            return 0
        elif self.cache_head == self.cache_tail:
            return 1
        else:
            return '2+'

    def remove(self):
        # 链表内的节点访问次数相同
        if self.pre is not None:
            self.pre.nxt = self.nxt
        if self.nxt is not None:
            self.nxt.pre = self.pre

        pre = self.pre
        nxt = self.nxt
        # 删除节点
        self.pre = self.nxt = self.cache_head = self.cache_tail = None

        return pre, nxt

    def pop_head_cache(self):
        if self.cache_head is None and self.cache_tail is None:
            return None
        elif self.cache_head == self.cache_tail:
            cache_head = self.cache_head
            self.cache_head = self.cache_tail = None
            return cache_head
        else:
            cache_head = self.cache_head
            self.cache_head.nxt.pre = None
            self.cache_head = self.cache_head.nxt
            return cache_head

    def append_cache_to_tail(self, cache_node):
        if self.cache_head is None and self.cache_tail is None:
            self.cache_head = self.cache_tail = cache_node
        else:
            cache_node.pre = self.cache_tail
            cache_node.nxt = None
            self.cache_tail.nxt = cache_node
            self.cache_tail = cache_node

    def insert_after_me(self, freq_node):
        freq_node.pre = self
        freq_node.nxt = self.nxt

        # 注意处理这个节点
        if self.nxt is not None:
            self.nxt.pre = freq_node

        self.nxt = freq_node

    def insert_before_me(self, freq_node):
        freq_node.nxt = self
        freq_node.pre = self.pre
        if self.pre is not None:
            self.pre.nxt = freq_node

        self.pre = freq_node