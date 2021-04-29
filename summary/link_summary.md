# 链表题型总结
链表题很多都可以通过以下几种方式单独和混合使用的方式解答。
### 倒数第K个节点 
```python
"""
当要返回倒数第k个节点时，k参数传递 k+1
当要删除倒数第k个节点时，k参数传递 k
为了统一处理这两种情况，head 需要传递虚拟节点 dummy
# 涉及到的题目：
19. 删除链表的倒数第 N 个结点
剑指 Offer 22. 链表中倒数第k个节点
61. 旋转链表 
    # 旋转k次，k可能大于链表长度，需要先进行 k = k mod len(list) ，然后倒数第k个节点处断开，
    # 传入k+1
    
# 这里没有处理k大于链表长度的问题，一般题目中都明确说明了k的大小
# 但是，面试的时候有可能需要处理一下
"""
def kth_node(head: ListNode, k: int) -> ListNode:
    s, f = head, head

    for i in range(k):
        f = f.next
    # 让f最终指向None节点
    while f:
        f = f.next
        s = s.next

    return s
```

### 中间节点
```python
"""
处理中间节点
题目：876 链表的中间结点 适用类型1  
面试题 02.06	回文链表 适用类型2 
109. 有序链表转换二叉搜索树 适用类型3
"""

"""
类型1： 返回中间靠后的节点
1     2     3  |    4    None     |
f           f  |           f      |
s     s     s  |                  |
从上图中可以看出
如果last_node 在3， s在2处返回   - 奇数个节点
如果last_node 在4， s在3处返回   - 偶数个节点
"""

def mid_node_after(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    s, f = head, head
    while f and f.next:
        s = s.next
        f = f.next.next
    return s

"""
类型2： 返回中间靠前的节点
1     2     3  |    4    None     |
f           f  |           f      |
s     s     s  |                  |
从上图中可以看出
如果last_node 在3， s在2处返回   - 奇数个节点
如果last_node 在4， s在2处返回   - 偶数个节点
"""
def mid_node_before(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    s, f = head, head.next  # 变化的地方 f = head.next
    while f and f.next:
        s = s.next
        f = f.next.next
    return s

"""
类型3： 根据首尾确定中间节点，上面的两种写法是针对一个完整链表求中间节点的
       如果同时指定了head 和 tail 节点，只需要针对上面的两种写法稍微做些调整就可以
eg: 例如下面的这种写法 tail = None 就变成了 mid_node_after
"""

def mid_node(head: ListNode, tail: ListNode) -> ListNode:
    if head == tail or head.next == tail:
        return head
    s, f = head, head
    while f != tail and f.next != tail:
        s = s.next
        f = f.next.next
    return s
```

### 链表的翻转
#### 迭代写法
```python
"""
翻转链表
通用写法： 接收head 和 tail，前开后闭区间 [head, tail)
eg: A->B->C->D->E->F->None
    翻转B->C->D 这段   head = B, tail = E 
相关题：
206. 翻转链表 
25. K 个一组翻转链表  
剑指 Offer 06 从尾到头打印链表
92 反转链表 II  
面试题 02.06	回文链表  
445	两数相加 II  
143. 重排链表
234	回文链表  
剑指 Offer 06 从尾到头打印链表  
369. 给单链表加一
"""
"""
迭代写法
A->B->C->D->E->None
tail = None

翻转步骤 - 细化

翻转后的链表                  翻转前的链表
None                        A->B->C->D->E->None
第一步：A->None              B->C->D->E->None
第二步：B—>A->None           C->D->E->None
第三步：C->B->A->None        D->E->None
第四步：D->C->B->A->None     E->None
第五步：E->D->C->B->A->None  None
完成翻转
从上面的步骤中可以看出
每次执行变更前，需要记住拆开后的两个链表的头部节点
pre 表示翻转后的链表的头节点 
head 表示翻转前的链表的头节点

需要完成下面的变化
    pre = None  head = A
    变成
    pre = A     head = B
    pre = B     head = C
    pre = C     head = D
    pre = D     head = E
    pre = E     head = None

可以通过这种逻辑完成
    tmp = head.next
    head.next = pre
    pre = head
    head = head.next

出口条件： head is not None

最后返回pre 就是我们想要的结果
时间复杂度：O(n)  n表示链表的长度
空间复杂度：O(1)  只利用了tmp pre 这两个变量，所以是常数个变量
"""
def reverse(head: ListNode, tail: ListNode) -> ListNode:
    pre = tail
    while head != tail:
        tmp = head.next
        head.next = pre
        pre = head
        head = tmp
    return pre

```
#### 递归写法
```python
"""
解题思路
A->B->C->D->E->None
出口条件 node.next is None  因为E.next is None,翻转后的头节点为E
语句1: D.next.next = E
语句2: D.next = None
语句1 和 语句2 可以将 D->E->None  转成 E->D->None

怎么把D.next 变成C？
C.next.next = D
C.next = None 
这样就可以把D.next 变成C了 

以此类推，可以完成E->D->C->B->A->None

总结下语句：
head.next.next = head
head.next = None

怎么返回E呢？
    出口条件处记录了节点E，可以把这个节点作为函数的返回值传回来

时间复杂度：O(n) n 表示链表的长度，递归遍历链表
空间复杂度：O(n) n 表示链表的长度，主要开销是栈的空间
"""
def reverse_list_recursion(head: ListNode, tail: ListNode) -> ListNode:
    # not head 可以兼容输入为空节点的情况
    # 出口条件
    if head == tail or head.next == tail:
        return head
    # 递归的执行翻转
    next_node = reverse_list_recursion(head.next, tail)

    # A->B  -->  B->A
    head.next.next = head
    head.next = tail
    # 每次都返回出口条件返回的结果
    return next_node
```
 
### 链表合并

 - 有序链表合并 
 ```python
"""
类型1： k个有序链表的合并 k >= 2

nums = [[1,4,5], [1,3,4], [2,6]]   0     2
left:      start 0  end   1
right:     start 2  end   2  return [2, 6]
left 继续拆分
left_l = start 0  end 0      return [1,4,5] 
left_r = start 1  end 1      return [1,3,4]

开始回归：
left_l  和left_r merge => [1,3,4,4,5]
继续和[2,6] merge
==>  [1,2,3,4,4,5,6]
"""

from typing import List


def merge_list(l1: ListNode, l2: ListNode) -> ListNode:
    """
    两个有序链表的合并
    """
    dummy = ListNode(0)
    head = dummy
    while l1 and l2:
        if l1.val < l2.val:
            head.next = l1
            l1 = l1.next
        else:
            head.next = l2
            l2 = l2.next

        head = head.next

    left_l = l1 or l2
    head.next = left_l
    return dummy.next
```
 - 交叉合并
 
```python
"""
类型2：交叉合并 
l1: A->B->C->D->None
l2: E->F->G->None
l1 merge l2: => A->E->B->F->C->F->D->None
"""
def merge(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(-1)
    new_node = dummy

    while l1 and l2:
        new_node.next = l1
        new_node.next.next = l2

        l1 = l1.next
        l2 = l2.next
        new_node = new_node.next.next

    # 别忘记处理l1
    new_node.next = l1
    return dummy.next
```
 
### 链表检测是否有环
```python

"""
141.环形链表
算法有效性证明
假设链表内有环
链表如下：
|---k----|
A->B->C->D->E-->F
        |       |
        |       |
        J<--I<- H

我们先认为这种算法是行的通的，只要证明其合理性就可以
假设：
    在H点相遇
    D-->H的距离为y
    环的长度为l
    A-->D 的长度为k
slow 表示慢指针
fast 表示快指针

相遇的时候
    slow走的总的路径长度 = k + pl + y
    fast走的总的路径长度 = k + ql + y    q > p,因为fast走的快

因为快指针的走的路径长度是慢指针的两倍，所以：
2 * (k + pl + y) = k + ql + y
k + y = (q - 2p) * l                  【M】
如果，取
    q = k, p = 0, y = kl - k

左等式： k + y = k + kl - k = kl
右等式   (q - 2p) * l = kl
因此，可以找到相遇的点

问题2: 怎么找到环的入口节点？
对公式M进行简化，取z = q-2p，则：k + y = z*l =>  k = z * l - y
让慢指针回到链表的头节点，调整快指针的步长为1，
z的取值为 1，2，3，4，.....
慢指针走k个节点，快指针走z * l - y个节点，也就是 (z - 1) * l + l - y,
所以他们必然会在D节点相遇，也就找到了入口节点。
时间复杂度：O(n)
空间复杂度：O(1)

"""
def has_cycle(head: ListNode) -> bool:
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        # fast 和 slow 中如果没有环，不可能同时为空，所以可以排除同时为空的场景
        # 如果有环，这里不可能为空，所以肯定是在环中相遇了
        if fast == slow:
            return True
    return False


def detectCycle(head: ListNode) -> ListNode:
    # 边界条件处理
    if not head or not head.next:
        return
        
    slow, fast = head, head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
        
    slow = head

    while slow and fast:
        if slow == fast:
            return slow
        slow = slow.next
        fast = fast.next
    return None
``` 
 
### 链表去重
 - 保留重复节点
 ```python
def deleteDuplicates(head: ListNode) -> ListNode:
    cur = head
    while cur and cur.next:
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head
```

 - 删除重复节点
 ```python
def delete_duplicate(head: ListNode) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    head = dummy
    while head and head.next and head.next.next:
        if head.next.val == head.next.next.val:
            # 找到重复节点 去重复
            to_remove = head.next.val
            while head and head.next and head.next.val == to_remove:
                if head.next.val == to_remove:
                    head.next = head.next.next
            continue
        else:
            head = head.next
    return dummy.next
```
 
### 链表排序
 - 合并排序算法思想
 用到的思想就是递归 + 取中间节点 + 合并有序链表
 ```python
def sort_list(head: ListNode, tail: ListNode) -> ListNode:
    # 边界条件处理
    if head is None:
        return head
    if head.next == tail:
        head.next = None
        return head

    # 取中间节点
    slow, fast = head, head
    while fast != tail and fast.next != tail:
        slow = slow.next
        fast = fast.next.next

    s_l = sort_list(head, slow)
    s_r = sort_list(slow, tail)
    return merge_sorted_link(s_l, s_r)
```

### 其他题目
 - 删除总和为零的连续节点
 ```
 """
1171. 从链表中删去总和值为零的连续节点
A->B->C->D->E->F->D->None
原理：如果A->...->F sum 为 100
     并且A->...->C sum 为 100
     说明D->...->F sum 为 0
     
     2. 在遍历节点不断推进的过程中，sum相同的节点会被后面的节点覆盖
    0   1   2    3    4   5    6
eg: 1-->2-->3-->-3-->-2-->3-->-3
sum 1   3   6    3    1   4    1

hash = {1: 6, 3: 3, 6: 3, 4: 4}

第一个节点的sum 等于最后一个节点的sum，第二次遍历仅仅执行了第一个节点就完成了
    
一次遍历获取截止到每个节点的sum，key 为sum，value 为 node
再进行一次遍历，利用上面的原理，获得sum 为0的区间，删除

注意事项：头节点可能会被删除，所以需要建立value 为0的虚拟节点
时间复杂度：O(n)
空间复杂度：O(n) 
"""
 ```
 - 公共节点
 ```python
"""
剑指 Offer 52. 两个链表的第一个公共节点
解题思路：
A1---->A2------>C1---->C2------>C3
              /
             B3
             |
B1---->B2----|

假设相遇点为C1:
记A1---C1    的长度为 X
记B1---C1    的长度为 Y
记C1---C3    的长度为 Z

那么，让A沿着A1->C1->C3  结束后，从B1开始走
让B沿着B1->C1->C3  结束后，从A1开始走
   
A     A1  A2  C1  C2   C3  B1  B2   B3   C1      X + Z  + Y
B     B1  B2  B3  C1   C2  C3  A1   A2   C1      Y  + Z + X
最终在C1相遇

如果两个链表不相交
A1--->A2---->A3--->None
B1---->B2-->None

时间复杂度：O(n)
空间复杂度：O(1)

# 这是要求在空间复杂度为O(1)的情况下，处理的
如果不要求O(1)，可以使用hash 和两次遍历的方式完成
"""
```
 - 复制带随机指针的链表
```python
"""
解题思路：复制每一个节点，存储在该节点之后。
eg: 现有链表 
    A->B->C->D->None
复制之后：
    A->A'->B->B'->C->C'->D->D'->None

其中A'是对复制A.val的新节点
这样我们就可以很方便的处理对随机节点的复制
eg: 假设，A.random 指向C，
    我们可以通过A.random.next 得到对random复制的节点
时间复杂度：O(n)
空间复杂度：O(n)
"""
```
 - 插入排序
 ```python
"""
147. 对链表进行插入排序
排序过程中链表的头节点可能会发生变化
1. 定义虚拟节点 dummy->head
2. 确定已经排序完成的链表的尾部节点 last_sorted，初始化为head
3. 开始进行选择排序，从cur = head.next 节点开始
4. case 1: cur.val >= last_sorted.val => 更新last_sorted
   case 2: cur.val < last_sorted.val 
           从dummy.next 开始找合适的节点，node.next.val > cur.val
           将cur 从原来的位置移除掉 last_sorted.next = cur.next
           将cur 插入到node的后面 tmp = node.next; node.next = cur;cur.next=tmp
           更新cur = last_sorted.next 继续执行第四步
5. 返回dummy.next

时间复杂度：O(n^2)
空间复杂度：O(1)
"""
```
### 链表设计题
单链表
双链表
环形链表
多重链表 - 跳表

### 应用场景
- 多项式相加 
- 多项式相乘
- 基数排序