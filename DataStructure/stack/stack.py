
from __future__ import annotations
class minStack(object):
    # design a stack that supports push and pop and top operations,
    # and can retrive the smallest element in a constant time
    # you can use ordered list to implement the stack
    # rember the min value
    def __init__(self):
        self.stack = []
        self.min = []
    
    def pop(self):
        if not self.stack:
            raise ValueError("empty stack")
        res = self.stack.pop()
        self.min.pop()
        return res

    def top(self):
        if not self.stack:
            raise ValueError("empty stack")

        return self.stack[-1]

    def get_min(self):
        if not self.stack:
            raise ValueError("empty stack")
        return self.min[-1]

    def push(self, value):
        self.stack.append(value)
        if not self.min:
            self.min.append(value)
        else:
            peek = self.min[-1]
            if peek > value:
                self.min.append(value)
            else:
                self.min.append(peek)


from enum import Enum
class Operate(Enum):
    add = '+'
    subtract = '-'
    multipy = '*'
    divide = '/'


def evaluate_reverse_polish_notation(tokens: []) -> int:
    # ["2", "1", "+", "3", "*"] = 9
    # explain: ((2+1) * 3) = 9
    operates = [item.value for item in Operate]
    stack = []
    for item in tokens:
        if item in operates:
            if len(stack) < 2:
                break
            a = stack.pop()
            b = stack.pop()

            if item == Operate.add.value:
                v = a + b
            elif item == "-":
                v = a - b
            elif item == "*":
                v = a * b
            elif item == "/":
                v = a / b
            stack.append(v)
        else:
            stack.append(int(item))
    v = stack.pop()
    return int(v)


def decode_string(a: str) -> str:
    # given an encoded string, return its decoded string.
    # eg: s = "3[a]2[bc]" , return aaabcbc
    # eg: s = "3[a2[c]]", return accaccacc
    stack = []
    for char in a:
        if char == ']':
            tmp = []
            while stack and stack[-1] != '[':
                tmp.append(stack.pop())
            if stack:
                stack.pop()  # pop [
            num = []
            # get number
            while stack and stack[-1] > '0' and stack[-1] < '9':
                num.append(stack.pop())
            number = int("".join(num[::-1]))

            for i in range(0, number):
                stack.extend(tmp)
        else:
            stack.append(char)
    return "".join(stack)


def dfs(root, target):
    # dfs recursive search template using using stack
    stack = [root]
    while stack:
        node = stack.pop()
        #--------
        if node.value == target:
            return node
        #--------

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)


def binary_lnr():
    
    pass


from typing import List


class Node(object):
    def __init__(self, val: int, neighbors: List[Node]):
        self.val = val
        self.neighbors = neighbors


# Definition for a Node.
class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        visited = {}
        return self.clone(node, visited)
    
    def clone(self, node, visited):
        if node is None:
            return
        if node in visited:
            return visited[node]
        new_node = Node(node.val)
        visited[node] = new_node
        for item in node.neighbors:
            new_node.neighbors.append(self.clone(item, visited))
        return new_node


class Ilands(object):
    grid = [['1', '1', '1'],
            ['1', '0', '0'],
            ['1', '0', '1']]

    def __init__(self, grid):
        self.grid = grid
        self.h = len(self.grid)
        self.w = len(self.grid[0])
        self.h_offset = [-1, 1, 0, 0]
        self.w_offset = [0, 0, -1, 1]

    def set_zero(self, i, j):
        self.grid[i][j] = 0
        for index in range(4):
            new_i = i + self.h_offset[index]
            new_j = j + self.w_offset[index]
            if new_i < 0 or new_i >= self.h or new_j < 0 or new_j >= self.w:
                continue
            if int(self.grid[new_i][new_j]) == 1:
                self.set_zero(new_i, new_j)

    def get_count(self):
        i_count = 0
        for i in range(self.h):
            for j in range(self.w):
                print(self.grid[i][j], i_count)
                if int(self.grid[i][j]) == 1:
                    self.set_zero(i, j)
                    i_count += 1
                print(self.grid)
        return i_count

res = Ilands(Ilands.grid).get_count()
print(res)

"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。
"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        pass
        # 边界条件检查
        size = len(heights)
        if size == 0:
            return 0
        if size == 1:
            return heights[0]
        heights = [0] + heights + [0]
        size += 2
        stack = [0]
        area = 0
        for index in range(1, size):
            while stack and heights[index] < heights[stack[-1]]:
                peek = stack.pop()
                width = index - stack[-1] - 1
                height = heights[peek]
                area = max(width * height, area)
            stack.append(index)
        return area

