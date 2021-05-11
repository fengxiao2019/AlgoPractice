

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