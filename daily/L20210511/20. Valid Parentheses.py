
"""
stack = []
遇到"(" "{" "[" 这种入栈
遇到闭合括号 ")" "}" "]" 出栈
闭合括号的上一个字符如果不匹配，返回False
如果stack最后非空，返回False
时间复杂度：O(n)
空间复杂度：O(n)
"""


def isValid(s: str) -> bool:
    stack = []
    hash_map = {')': '(', '}': '{', ']': '['}
    for item in s:
        if item in hash_map.values():
            stack.append(item)
        else:
            if not stack or hash_map[item] != stack.pop():
                return False
    return stack == []