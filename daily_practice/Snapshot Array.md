1146. Snapshot Array 
实现支持下列接口的「快照数组」- SnapshotArray：

SnapshotArray(int length) - 初始化一个与指定长度相等的 类数组 的数据结构。初始时，每个元素都等于 0。
void set(index, val) - 会将指定索引 index 处的元素设置为 val。
int snap() - 获取该数组的快照，并返回快照的编号 snap_id（快照号是调用 snap() 的总次数减去 1）。
int get(index, snap_id) - 根据指定的 snap_id 选择快照，并返回该快照指定索引 index 的值。

**版本1**
最容易想到也是在业务设计过程中常用的方式就是直接保存整个快照
```python
records 设计为List[List[int]]，作为快照容器，在snap函数调用时，将当前快照添加进records中。
存在的问题：copy了整个快照信息，比较占用内存，测试案例过不去。
```

**优化**
新的设计方案，records的容量为capacity。每一个槽对应一个链表，链表的元素为`snap_id, val`。这样，在snap时就避免了copy。
数据结构形式如下：
![设计图][image-1]
```python
class SnapshotArray:
    """
    快照存在一个列表中，每个快照有一个索引
    """
    def __init__(self, length: int):
		# 关键在这里的设计
        self.records = [[[-1, 0]] for _ in range(length)]
        self.snap_id = 0

        

    def set(self, index: int, val: int) -> None:
        self.records[index].append([self.snap_id, val])
        

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1
        

    def get(self, index: int, snap_id: int) -> int:
        i = bisect.bisect_left(self.records[index], [snap_id + 1]) - 1
        return self.records[index][i][1]
        
```

[image-1]:	https://tva1.sinaimg.cn/large/008i3skNly1gq1gy95668j30tw0co3zc.jpg