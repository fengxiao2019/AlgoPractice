"""
因为‘#’ 涉及到删除操作，所以可以使用stack模拟这种操作
eg: ab#c => [a] => 遇到b=> [ab] => 遇到# => [a] => 遇到c => [ac]
ad#c => [a] => [ad] => [a] => [ac]
时间复杂度：O（max(len(s), len(t))
空间复杂度：O(max(len(s), len(t))
"""


def backspace(s: str) -> bool:
    stack = []
    for item in s:
        if item == '#':
            if stack: stack.pop()
        else:
            stack.append(item)
    return stack