LRU缓存
### 实现方法1
**思路**
采用OrderedDIct 实现
**代码**
```python
from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]


    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
```

### 实现方法2
**双向链表 + hash 表**
**代码**
```python
class Node:
    def __init__(self, key: int, value: int, prev: 'Node'=None, nxt: 'Node'=None) -> None:
        self.key = key
        self.value = value
        self.prev = prev
        self.nxt = nxt

    def __str__(self):
        return f'({self.key}, {self.value})'
"""
思路： 为了方面处理插入，删除，添加两个虚拟节点 head 和 tail
get -> 调整到tail
put -> 1. 存在 更新-> 调用一次get
       2. 不存在，插入，检查容量
"""
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.head = Node('head', 'head')
        self.capacity = capacity
        self.tail = Node('tail', 'tail')
        self.head.nxt = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        node = self.cache[key]
        # node 的前节点 连接到 node 的后节点
        node.prev.nxt = node.nxt
        # node 的后节点 连接到 node 的前节点
        node.nxt.prev = node.prev
        # 上面两个动作完成了node的删除动作
        # 现在要把node 调整到尾部
        self._put_to_tail(node)
        # 返回值
        return node.value
    
    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # 创建节点
            node = Node(key, value)
            # 将节点加入到尾部
            self._put_to_tail(node)
            # 添加到cache中
            self.cache[key] = node
            # 检查容量
            self.check_capacity() 
        else:
            # node 的value
            node = self.cache[key]
            node.value = value
            # 更新节点的位置
            self.get(node.key)

    def _put_to_tail(self, node:Node) -> None:
        node.nxt = self.tail
        node.prev = self.tail.prev
        self.tail.prev.nxt = node
        self.tail.prev = node
        
    def check_capacity(self):
        if len(self.cache) > self.capacity:
            self.cache.pop(self.head.nxt.key)
            self.head.nxt = self.head.nxt.nxt
            self.head.nxt.prev = self.head
```
