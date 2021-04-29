# trie
## 介绍
Trie也称为前缀树，是一种搜索树，是一种用于从一个集合中定位特定键的树状数据结构。最长见的键是字符串，节点之间的链接是由键中的字符确定的，节点中存储的也是字符。

与二叉树的区别：
>    trie 存储的不是整个字符串，而是串中的字符，一个节点的位置决定了这个字符关联了哪些字符串。

**Trie 树数据结构**

 - Alphabet 表示字符集合 
 - 假设S是一组字符串（串中的字符源于Alphabet）
 - Trie 是一种存储S中字符的树形结构
 - 特征：
	 1. 每个节点都包含一个字符（root节点除外）
	 2. 每个叶子节点都关联了一个字符串
	 3. 节点按照字符串中的字符顺序进行排序
	 3. 从根节点到叶子节点这条路径会生成一个字符串 
		 
S = { bear, bell, bid, bull, buy, sell, stock, stop }         (s = 8)  
![][image-1] 

## Trie vs Hash
Trie的优点
 - 查询时间O(k), k 指的是key的size。
 - 如果没有的话，查找的时间小于k
 - 支持前缀匹配查询 
 - 不需要哈希函数, 没有碰撞问题
因此，可以看出，如果你需要是精确匹配，那么hash更合适，但是如果你还需要前缀匹配这个场景，Trie树更合适。
 
## Trie 的实现
```python
from typing import Dict, List
from typing import Optional

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children: Dict[str: 'Trie'] = {}
        self.is_end: bool = False
        

    # 插入
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
        node.is_end = True
    
    # 搜索
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self._getNode(word)
        if node is None or node.is_end is False:
            return False
        return True


    # 自动补全功能
    def _collects(self, x: Optional['Trie'], prefix: List[str], results: List[str]) -> List['Trie']:
        if x is None:
            return None
        
        prefix_str = "".join(prefix)
        results.append(prefix_str)
        for char in x.children:
            # 回溯算法
            prefix.append(char)
            self._collects(x.children[char], prefix, results)
            del prefix[-1]

    def keysWithPrefix(self, prefix: str) -> List[str]:
        results: List[str] = []
        node = self._getNode(prefix)
        self._collects(node,list(prefix), results)
        return results
    
    def _getNode(self, key: str) -> Optional['Trie']:
        node = self
        for char in key:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
                
    
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self._getNode(prefix) is not None

    """
    键的删除可以懒惰地进行（只清除键对应的节点内的值），也可以马上清理任何不再需要的父节点。
    这里给出马上删除的例子
    """
    def delete(self, prefix: str) -> bool:
        
        def _delete(node: 'Trie', key: str, d: int) -> bool:
            if d == len(key):
                return 
            else:
                c = key[d]
                if c in node.children and _delete(node.children[c], key, d + 1):
                    del node.children[c]
                return len(node.children) is None
        return _delete(self, prefix, 0)
```

### radix tree (压缩 Trie树)
表示一个空间优化的 trie（前缀树），如果父节点只有一个子节点，将子节点合并到父节点。
![][image-2]
所以，每个内部节点（我们称叶子节点为外部节点）的子节点的数量\>= 2


## 设计搜索引擎

### 相关技术
搜索（爬虫技术） -\> 预处理（分词） --\> 索引(倒排索引) --\> 查询(Trie)

### 倒排索引 inverted Tree

以ES为例子，里面有两个关键术语
 - term: 指搜索词项（搜索时不会再对其进行拆分）
 - posting list：包含特定term的文档id的集合
	 
简单过程就是：对文档内容进行分词，提取term，根据关键词建立倒排索引，倒排索引的结构就是每一个term 关联一个posting list。

问题1： 海量term，怎么存储？
对term进行排序，然后二分查找。这样的可以使用logN 次磁盘查找得到目标。但是磁盘的随机访问非常耗时（一次random access大概10ms）。仍然需要优化，尽量减少磁盘的随机访问次数，所以引出问题2。

问题2： 海量term存储在内存中存不下，只能放磁盘，放磁盘，访问的时候就会触发很多次磁盘的随机访问，在这种情况下，如何优化？
> 针对term建立索引，term index，term index是一颗Trie树，从term index可以快速找到term在term dictionary中偏移量(offset)，然后从这个位置再往后顺序查找，大大减少磁盘随机访问的时间，而且，压缩后的term index 容量非常小，可以全部放入内存中。

问题3： term index 如何存储的？
> FST(finite state transducers) 
> > - 空间占用小。通过对词典中单词前缀和后缀的重复利用，压缩了存储空间
> > - 查询速度快。O(len(str)) 的查询时间复杂度。
> 
> FST 的存储内容: \<单词前缀，以该前缀开头的所有Term的压缩块在磁盘中的位置\>
> 
> term dictionary 在磁盘中是按块存储的，一个 block 内部利用公共前缀压缩。

[image-1]:	../images/trie02.gif
[image-2]:	../images/trie08.gif