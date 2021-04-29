# [207] 课程表
#
from typing import List
from collections import defaultdict, deque
# @lc code=start


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # step1: 构造图
        edges = defaultdict(list)
        indegs = [0] * numCourses
        for edge_s, edge_e in prerequisites:
            edges[edge_s].append(edge_e)
            indegs[edge_e] += 1  # 入度统计
        # step2: 构造队列
        q = deque()
        for i in range(numCourses):
            if indegs[i] == 0:
                q.append(i)
        # step3: 遍历队列，统计节点的个数
        v_count = 0
        while q:
            v = q.popleft()
            v_count += 1
            for adj in edges[v]:
                indegs[adj] -= 1
                if indegs[adj] == 0:
                    q.append(adj)
        return v_count == numCourses

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 先构造图
        edges = defaultdict(list)

        for edge_s, edge_e in prerequisites:
            edges[edge_s].append(edge_e)

        # 每个节点的访问状态可以有三种
        # 0: 未搜索 1: 搜索中 2: 搜索完
        visited = [0] * numCourses
        valid = True

        def dfs(u: int):
            # 深度优先搜索算法
            nonlocal valid
            visited[u] = 1  # 标记u为搜索中

            # 处理相邻节点
            for adj in edges[u]:
                if not valid:
                    return
                if visited[adj] == 0:
                    dfs(adj)
                elif visited[adj] == 1:
                    # 如果在搜索中的节点遇到搜索中的节点
                    # 说明有环
                    valid = False
                    return
            visited[u] = 2

        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)
        return valid