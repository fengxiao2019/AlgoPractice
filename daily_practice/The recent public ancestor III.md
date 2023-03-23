1650. 二叉树的最近公共祖先 III
**描述**
给定一棵二叉树中的两个节点 p 和 q，返回它们的最近公共祖先节点（LCA）。
** 每个节点都包含其父节点的引用（指针）。Node 的定义如下：
```c
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
```
**代码**
```c
"""
解题思路：因为node节点中记录了父节点，可以把父节点利用起来。
先从p节点开始，用visited 记录p到root路径上的所有节点。
然后从q节点开始，首个出现在visited中的节点，就是第一个最近公共父节点
时间复杂度：O(h) h 指树的高度
空间复杂度：O(h) h 指数的高度
"""
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        visited = set()
        while p:
            visited.add(p)
            p = p.parent
        while q:
            if q in visited:
                return q
            q = q.parent
        return None

    """
    思路：实际可以看成是两个链表相遇的节点
    时间复杂度：O(h)
    空间复杂度：O(1)
    """ 
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        node1, node2 = p, q
        while node1 and node2:
            node1 = node1.parent if node1.parent else q
            node2 = node2.parent if node2.parent else p
            if node1.val == node2.val:
                return node1
        return None
```
