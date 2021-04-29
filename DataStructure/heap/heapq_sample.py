class MinFixedHeap(object):
    def __init__(self, k: int):
        self.fixed_size = k
        self.heap = []

    def insert(self, val):
        if len(self.heap) < k:
            heapq.heappush(self.heap, val)
        else:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]

import heapq
import collections
class Solution:
    def topKFrequent(self, nums, k):
        counter = collections.Counter(nums)
        heap = []
        for _, v in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, v)
            else:
                heapq.heappushpop(heap, v)
        return heapq

  
so = Solution()
test_cases = {"1":  [[1, 1, 1, 2, 2, 3], 2]}
for k, v in test_cases.items():
    print(so.topKFrequent(v[0], v[1]))


# 什么是拓扑排序
# 在图论中，拓扑排序是一个有向无环图（DAG）的所有顶点的线性序列，且该序列必须满足下面两个条件：
# 每个定点出现且只出现一次
# 如果存在一条从定点A到定点B的路径，那么在序列中定点A出现在定点B的前面。
# DAG才有拓扑排序，非DAG没有拓扑排序


from collections import defaultdict
from typing import List
import abc


class GraphInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'addEdge') and
                callable(subclass.addEdge) and
                hasattr(subclass, 'topologicalSort') and
                callable(subclass.topologicalSort)
                )

    @abc.abstractmethod
    def addEdge(self, v: int, w: int):
        raise NotImplementedError

    @abc.abstractmethod
    def topologicalSort(self):
        raise NotImplementedError


class GraphVersion1(GraphInterface):
    def __init__(self, v_count: int):
        """
        :param v_count: 定点的个数
        """
        self.v_count = v_count  # 定点的个数
        self.adj = defaultdict(list)  # 临接表
        self.q = []  # 入度为0的定点的集合
        self.indegrees = [0] * self.v_count

    def addEdge(self, v: int, w: int):
        self.adj[v].append(w)
        self.indegrees[w] += 1

    def topologicalSort(self):
        res = []
        for i in range(self.v_count):
            if self.indegrees[i] == 0:
                self.q.append(i)

        count = 0
        while self.q:
            v = self.q.pop(0)
            count += 1
            res.append(v)
            for item in self.adj[v]:
                self.indegrees[item] -= 1
                if self.indegrees[item] == 0:
                    self.q.append(item)
        if count < self.v_count:
            raise Exception("find cycle")
        return res


class Graph(object):
    def __init__(self, v: int):
        """
        :param v: 定点的个数
        """
        self.v = v
        self.adj = defaultdict(list)

    def addEdge(self, v: int, w: int):
        """
        构造图
        :param v: 边的一个顶点
        :param w: 边的另一个定点
        :return:
        """
        self.adj[v].append(w)

    def topologicalSortUtil(self, v: int, visited: List[int], stack: List[int]):
        visited[v] = True
        for item in self.adj[v]:
            if not visited[item]:
                self.topologicalSortUtil(item, visited, stack)
        stack.append(v)
        print(stack)

    def topologicalSort(self):
        stack = []
        visited = [False] * self.v
        for i in range(self.v):
            if visited[i] is False:
                print(f"enter: {i}")
                self.topologicalSortUtil(i, visited, stack)

        while stack:
            print(stack.pop())

# 拓扑排序思想2
# step1: 从DAG中选择一个没有前驱（即入度为0）
# step2: 从图中删除该定点和所有以它为起点的有向边
# step3: 重复1和2直到当前的DAG为空或者图中不存在入度为0的顶点为止，后面一种情况说明DAG中有环


def main():
    graph = GraphVersion1(6)
    graph.addEdge(5, 2)
    graph.addEdge(5, 0)
    graph.addEdge(4, 0)
    graph.addEdge(4, 1)
    graph.addEdge(2, 3)
    graph.addEdge(3, 1)
    res = graph.topologicalSort()
    print(res)

import sys
def shortest_path(graph):
    v_count = len(graph)
    graph = GraphVersion1(6)
    graph.addEdge(1, 2)
    graph.addEdge(1, 3)
    graph.addEdge(2, 7)
    graph.addEdge(3, 2)
    graph.addEdge(3, 5)
    graph.addEdge(4, 6)
    graph.addEdge(5, 4)
    graph.addEdge(5, 6)
    max_size = sys.maxsize - 1
    v_hash = {1: 0, 2: max_size, 3: max_size, 4: max_size, 5: max_size, 6: max_size}
    for i in range(1, 7):
        graph.adj[i]
if __name__ == '__main__':
    main()