"""
总结：重复元素的删除问题
相关问题：链表的重复删除问题
        数组的重复元素删除
        字符串重复删除 1047
        字符串连续k个重复元素删除问题 1048
"""

"""
因为是相邻重复项，可以使用栈来处理
时间复杂度：O(n)
空间复杂度：O(n)
"""

def removeDuplicates(s: str) -> str:
    stack = []
    for item in s:
        # [a, b]
        if stack and stack[-1] == item:
                stack.pop()
        else:
            stack.append(item)
    return "".join(stack)


"""
将字符串转成数组，用双指针解，其实也是模拟栈的行为
如果 i > 0 并且 res[i] == s[i-1] 说明有最近的两个元素重复了，
那么，res[i] 和 res[i - 1]这两个槽可以复用了，将指针指向res[i-1]这个槽
否则：res[0:i+1] 范围内的没有可以复用的槽，将当前指针指向res[i+1]这个槽

最后结果集中i前面的元素都是有效的数据
时间复杂度：O(n)
空间复杂度：O(n)
"""
def removeDuplicates(s: str) -> str:
    res = [item for item in s]
    # 定义结果集指针
    i = 0
    for j in range(len(res)):
        res[i] = res[j]
        if i > 0 and res[i - 1] == res[i]:
            i -= 1
        else:
            i += 1
    return "".join(res[:i])

"""
如果是将字符串中重复相邻的元素只保留一个呢？
eg: aaabbbcccc => abc
abbcc => abc
也可以复用上面的解题方式
时间复杂度：O(n)
空间复杂度：O(n)
"""
def removeDuplicate(s: str) -> str:
    res = [item for item in s]
    i = 0
    for j in range(len(res)):
        res[i] = res[j]
        if i == 0 or res[i - 1] != res[j]:
            i += 1
    return "".join(res[i])


"""
用栈来解决
如果当前元素和栈顶的元素不相等就添加到栈中
时间复杂度：O(n)
空间复杂度：O(n)
"""
def removeDuplicate(s: str) -> str:
    stack = []
    for item in s:
        if not stack or stack[-1] != item:
            stack.append(item)
    return "".join(stack)

"""
删除所有重复元素，复用模板
和1047的唯一区别是，元素连续的次数是奇数的话，会存储一次
"""

def removeAllDuplicates(s: str) -> str:
    stack = []
    to_del = None
    for item in s:
        if item == to_del: continue
        else: to_del = None

        if stack and stack[-1] == item:
            stack.pop()
            to_del = item
        else:
            stack.append(item)
    return "".join(stack)

"""
更简洁的写法, 套用删除链表中的重复节点的模板
时间复杂度：O(n)
空间复杂度：O(n)
"""
def removeAllDuplicates(s: str) -> str:
    stack = []
    i = 0
    while i < len(s):
        if i < len(s) - 1 and s[i] == s[i + 1]:
            to_del = s[i]
            while to_del == s[i]:
                i += 1
        else:
            stack.append(s[i])
            i += 1
    return "".join(stack)

"""
删除重复元素
"""
class LinkNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def removeDuplicateLink(root: LinkNode) -> LinkNode:
    # 需要借助虚拟节点
    dummy = LinkNode(-1)
    dummy.next = root
    head = dummy
    while head and head.next and head.next.next:
        if head.next.val == head.next.next.val:
            to_del = head.val
            while head.next and head.next.val == to_del:
                head.next = head.next.next
            head.next = head.next.next
        head = head.next
