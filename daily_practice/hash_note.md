解决冲突的方法：
  - 分离链接法 - 将散列到同一个值的所有元素保留到一个链表中。
	```
	- 缺点： 需要指针，由于给新的单元分配地址需要时间，导致算法的速度有些减慢，同时算法还要求对另一种数据结构的实现。
	- 装载因子 load factor 约等于 1
	```
  - 开放寻址法 - open addressing hashing. 
	```
	- 如果有冲突发生，就重试选择另外的单元，直到找出空的单元为止。hi(x) = (Hash(x) + F(i)) mod tablesize，函数F为解决冲突的方法。
	- 装填因子 低于0.5 

	- 线性探测法 
	    F(i) = i 相当于逐个探测每个单元（必要时可以绕回）以查找出一个空单元。
	    从下面的表格可以看出，当装填因子大于0.5，线性探测法就不是一个好的方法
	    缺点：当装填因子大于0.5时，探测次数会随着装填因子的增大而急剧上升，会有严重的一次聚集问题

	    装填因子    插入探测次数 

	    0.5           2.5
	    0.75          8.5
	    0.9           50     
	- 平方探测法: 目的是为了消除线性探测法中的一次聚集问题的冲突解决办法。
	    F(i) = i^2
	    一旦表被填满超过一半，当表的大小不是素数的时候甚至在表被填满一半之前，就不能保证一次找到一个空单元了。
	    这是因为最多有表表的一半可以用作解决冲突的备选位置。
	    如果表有一半是空的，并且表的大小是素数，那么我们保证总能够插入一个新的元素。
	    缺点：虽然排除了一次聚集，但是散列到同一位置上那些元素将探测相同的备选单元。这叫做二次聚集。

	- 双散列（double hashing）：F(i) = i * hash(X) i = 1 2 3 4 
	   hash2(X) = R - (X mod R) R是小于TableSize的素数，eg R = 7
	   hash2(49) = 7 - (49 mod 7) = 7 - 0 = 75
	```
  - 再散列：当表达到某一个装填因子时，进行再散列。一般为比2N大的一个素数。
		 

## 问题
### 为什么建议hash 表的大小是素数？
   - 将哈希表长度设置为一个大的质数，将大大减少碰撞的发生。
   - 如果表的长度可以分解为多个因子，每一个与长度有共同因子的整数都会被哈希成一个索引，这个索引是这个因子的倍数，如果可以分解的因子越多，那么出现的碰撞的几率就会越大，因此我们应该选择因子最少的数，质数只能分解成1和他自己，所以选择质数的话，会大大减少碰撞的几率。
### 什么是素数(质数)？
 - 如果一个数如果只能被 1 和它本身整除，那么这个数就是素数

### 如何寻找大于某个数的素数？如何判断一个数是否是素数？如何寻找某个范围内的素数？
```
import sys

```


### python dict 使用哪种方法处理冲突问题的？装填因子是多少？rehash的动作是怎样的？
因为链地址法会带来分配链表的开销，而 cpython 中 dict 又运用得极其普遍，
因此 dict 采用开放寻址法来实现哈希表 python dict 的实现使用了open addressing 方式来解决hash冲突问题。
当使用的slots 和 dummy slots 超过array的2/3时，就会触发数组的调整。
开放寻址的方式采用的双散列方式，双散列的方法如下：
``` python
# PERTURB_SHIFT 默认为5
# 
j = (5*j) + 1 + perturb;
perturb >>= PERTURB_SHIFT;
use j % 2**i as the next table index;
```

### redis 使用哪种方法处理冲突问题的？装填因子是多少？rehash的动作是怎样的？
### python 提供了几种dict？实现原理是什么？


### hash 的优点?
  - O(1)的查询和插入操作。
### hash 的缺点？
  - 虽然hash表的操作需要常量时间，但一个好的hash函数的运算成本可能比顺序列表或者搜索数的查找算法要高很多，所以，在数据量小的情况下，hash表并不高效。
  - 不保证插入顺序。Python 提供的dict 在3.7 版本之后保证有序了，但是还是建议使用OrderDict
  - 虽然每次操作的成本是常量的，但是在调整大小时需要的时间和实际的key的数量还是成正比的。
  - 当存在许多碰撞时，哈希表的效率会变得相当低下。
### 如何实现一个hash?
```python
class ListNode:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1001
        self.bucket = [None] * self.size

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        h_v = key % self.size
        if self.bucket[h_v] is None:
            self.bucket[h_v] = ListNode(key, value)
        else:
            cur = self.bucket[h_v]
            if cur.key == key:
                cur.val = value
                return

            while cur and cur.next:
                if cur.next.key == key:
                    cur.next.val = value
                    return
                else:
                    cur = cur.next
            cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        h_v = key % self.size
        head = self.bucket[h_v]
        if head is None:
            return -1
        while head:
            if head.key == key:
                return head.val
            else:
                head = head.next
        return -1

    def remove(self, key: int,key_ = """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """) -> None:
        key_
        h_v = key % self.size
        head = self.bucket[h_v]
        if head is None:
            return
        if head.key == key:
            self.bucket[h_v] = head.next
            return
        while head and head.next:
            if head.next.key == key:
                head.next = head.next.next
            else:
                head = head.next
```
### 如何避免一次性rehash？
一次性放大表的一个替代方法是逐步执行重合表。
 - 在调整大小的过程中，分配新的哈希表，但保持旧表不变。
 - 在每次查找或删除操作中，检查两个表。
 - 只在新表中执行插入操作。
 - 在每次插入时也将r个元素从旧表移到新表中。
 - 当所有的元素都从旧表中删除时，对其进行去分配。
为了保证在新表本身需要放大之前将旧表完全复制过来，在调整大小的过程中，有必要将表的大小至少增加一个系数（r+1）/r。 
### 如何衡量一个hash算法的好坏？
hash value 尽量均匀分布，少产生碰撞

### hash map 为什么使用什么类型的元素当作key？
 通常我们建议使用不可变类型作为hash的key。但是，默认情况下，所有用户定义的类型都可以作为字典键使用，hash(object)默认为id(object)，cmp(object1, object2)默认为cmp(id(object1), id(object2))。 
 在必须将对象放在映射中的情况下，对象标识往往比对象内容重要得多。
 在对象内容确实很重要的情况下，可以通过覆盖 __hash__ 和 __cmp__ 或 __eq__ 来重新定义默认设置。

### 如何实现一个不可变类？
   - 方法1 使用dataclasses
```python
from dataclasses import dataclass
@dataclass(frozen=True)
class Location:
    name: str
    longitude: float = 0.0
    latitude: float = 0.0
```

   -方法2 使用\_\_slot\_\_，同时禁止\_\_setattr\_\_ 和  __delattr__
```python
class Immutable:
    __slots__ = ('a','b')
    def __init__(self, a , b):
        super().__setattr__('a',a)
        super().__setattr__('b',b)

    def __str__(self):
        return "".format(self.a, self.b)

    def __setattr__(self, *ignored):
        raise NotImplementedError

    def __delattr__(self, *ignored):
        raise NotImplementedError
```
### 一致性hash算法
#### 介绍
一致性hash算法是一种特殊的散列方式，当hash表的大小需要调整时，平均只需要重新映射n/m个键，其中n是键的数量，m是槽的数量。在大多数传统的哈希表中，数组插槽数量的变化会导致几乎所有键被重新映射。

#### 场景
考虑到负载均衡这样一个场景，你有一批对象需要存储到一组服务器(n)上，通常我们对对象o做hash(o) mod n 来决定这个对象具体存储在哪台服务器上。但是这存在一个问题，当有一台服务器故障时，n的数量发生了变化，hash(o) mod n 变成了
hash(o) mod (n - 1)，这样绝大多数数据的存储节点都发生了变化，这就要求所有的数据都移动到新的服务器上。
一致性hash算法就是为了解决这种问题而出现的。
#### 原理
使用hash函数将服务器和对象映射到一个圆上，每个对象按顺时针顺序被分配到下一个出现在圆圈上的服务器，如果一个服务器发生故障并从圆圈中移除，只有映射到故障服务器的对象需要按顺时针顺序重新分配到下一个服务器。

#### 如何实现该算法？

> > https://www.laurentluce.com/posts/python-dictionary-implementation/
> http://pybites.blogspot.com/2008/10/pure-python-dictionary-implementation.html