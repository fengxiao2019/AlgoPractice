class Solution:
    def calculate(self, s: str) -> int:
        return calculate(s)


"""
3 + 2 * 2
表达式中只涉及到了数字字符 、空白字符、运算符字符（+ - / *）
+ ： 压入数字
- ： 压入数字取反
* ：当前数字 * stack.pop()，压入
/ : 这里是个坑，需要
时间复杂度：O(n)
空看复杂度：O(n)
"""


def calculate(s: str) -> int:
    stack = []
    num = 0
    op_map = {
        '+': lambda e: stack.append(e),
        '-': lambda e: stack.append(-e),
        '*': lambda e: stack.append(e * stack.pop()),
        '/': lambda e: stack.append(int(operator.truediv(stack.pop(), e)))
    }
    op = '+'
    for char in s + '+':
        if char == ' ':
            continue

        if char.isdigit():
            num = num * 10 + ord(char) - ord('0')
        else:
            op_map[op](num)
            op = char
            num = 0
    return sum(stack)