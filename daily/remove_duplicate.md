 场景3: 有序链表，重复的元素保留k个 ，k \>= 1
这个情况下，在场景1的代码上进行改造就能够完成
```python
def deleteDuplicates(head: ListNode, k: int) -> ListNode:
    cur = head
    count = 1
    while head and head.next:
        if head.val == head.next.val:
            if count == k:
                head.next = head.next.next
            else:
                count += 1
                head= head.next
        else:
            head = head.next
            count = 1
    return cur
```
[场景4: 有序数组，相邻重复的元素保留1个，原地删除 lc26][1] 
```python
"""
解题思路：
	要求原地删除
	用一个指针i记录当前满足条件的数据下标
	用另一个指针j遍历nums
	如果指针i指向的元素 和 指针j指向的元素不相等，说明j指向的元素是一个新的元素，可以更新到i+1的位置，更新i = i + 1
	当j 执行完时，i+1就是满足条件的长度
	时间复杂度：O(n)
	空间复杂度：O(1)
"""

def removeDuplicates(nums: List[int]) -> int:
	i, j = 0, 1
	for j in range(1, len(nums)):
    	if nums[i] != nums[j]:
        	i += 1
        	nums[i] = nums[j]
	return i + 1

"""
假如不要求原地删除，可以用一个额外的数组，结构更清晰
时间复杂度：O(n)
空间复杂度：O(1)
"""

def removeDuplicates_back(nums: List[int]) -> int:
	stack = []
	for i in range(len(nums)):
    	if not stack or stack[-1] != nums[i]:
        	stack.append(nums[i])
	return stack
```

场景6: 有序数组，重复的元素全部删除，原地删除
```python
"""
更简洁的写法, 套用删除链表中的重复节点的模板
时间复杂度：O(n)
空间复杂度：O(n)
"""
def removeAllDuplicates(nums: List[int]) ->List[int]:
    stack = []
    i = 0
    while i < len(nums):
        if i < len(s) - 1 and nums[i] == nums[i + 1]:
            to_del = nums[i]
            while i < len(s) and nums[i] == to_del:
                i += 1
        else:
            stack.append(nums[i])
            i += 1
    return stack
```
[场景6: 有序数组，重复的元素保留k个，原地删除.  LC 80][2]
```python
"""
关键词：有序 重复  原地 返回新长度

解题思路：双指针
用一个指针j遍历数组
用另一个指针i指向有效数据的位置
用一个变量count记录一个元素重复出现的次数

时间复杂度：O(n)
空间复杂度：O(1)
"""
def removeDuplicates(nums: List[int], k:int) -> int:
    count = 1
    i, j = 0, 1
    for j in range(1, len(nums)):
        # 如果两个值相等
        if (nums[i] == nums[j] and count < k) or nums[i] != nums[j]:
            count = 1 if nums[i] != nums[j] else count + 1
            nums[i+1] = nums[j]
            i += 1
    return i + 1
```
[场景7. 删除字符串中的所有相邻重复项 lc. 1047][3]
```python
"""
因为是相邻重复项，可以使用栈来处理
时间复杂度：O(n)
空间复杂度：O(n)
"""

def removeDuplicates(s: str) -> str:
    stack = []
    for item in s:
        if stack and stack[-1] == item:
            stack.pop()
        else:
            stack.append(item)
    return ''.join(stack)   

"""
将字符串转成数组，用双指针解决

"""
def removeDuplicates(s: str) -> str:
    res = [s for item in s]
    i = 0
    for j in range(len(s)):
        res[i] = s[j]
        if i > 0 and res[i] == res[i-1]:
            i -= 1
        else:
            i += 1
    return "".join(res[:i])
```
[场景8. 删除字符串中的所有相邻重复项 II  lc.1209][4]
> 给你一个字符串 s，「k 倍重复项删除操作」将会从 s 中选择 k 个相邻且相等的字母，并删除它们，使被删去的字符串的左侧和右侧连在一起。
> 你需要对 s 重复进行无限次这样的删除操作，直到无法继续为止。
> 在执行完所有删除操作后，返回最终得到的字符串。
```python
"""
解题思路：k个连续的字符才能删除
还是用栈来处理，栈的元素为(item, count) item为字符串中的字符，count为连续出现的次数
弹出栈的时机：count == k: 弹出
count 累加的时机：stack[-1][0] == cur_item => stack[-1][1] += 1
边界条件：len(s) < k : 返回s

时间复杂度：O(n)
空间复杂度：O(n)
"""

def removeDuplicates(s: str, k: int) -> str:
    if len(s) < k: return s
    stack = []
    for item in s:
        if not stack or stack[-1][0] != item:
            stack.append([item, 1])
        else:
            stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()
    res = ""
    for item in stack:
        res += item[0] * item[1]
    return res
```

场景9: 给定一个字符串，递归地从该字符串中删除相邻的重复字符。输出的字符串不应该有任何相邻的重复字符。
`Input: azxxzy         Output: ay`
```python
"""
套用场景7，在场景7中，相邻元素重复的次数如果是偶数次，就会全部清除
但是，如果是奇数次，就会留一个元素，我们可以利用这一点来处理这个问题
时间复杂度：O(n)
空间复杂度：O(n)
"""
def removeDuplicates(s: str) -> str:
    stack = []
    last_char = None
    for item in s:
        if stack and stack[-1] == item:
            last_char = stack.pop()
        else:
            if item != last_char:
                stack.append(item)
                last_char = None
    return ''.join(stack)   
```


[1]:	https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/
[2]:	https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/
[3]:	https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string/
[4]:	https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string-ii/