from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        def dfs(r: int, c: int):
            # 退出条件
            if dp.get((r, c)):
                return dp[(r, c)]

            #           上       下       左       右
            poses = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            best = 1
            for p_r, p_c in poses:
                # 未开始 & 已完结的 && value > cur_value
                n_r = r + p_r
                n_c = c + p_c
                if 0 <= n_r < r_len and 0 <= n_c < c_len and matrix[n_r][n_c] > matrix[r][c]:
                    best = max(best, dfs(n_r, n_c) + 1)

            dp[(r, c)] = best
            return dp[(r, c)]

        # step 1 定义相关数据解构
        dp = {}  # 存储已经计算出来的每个节点的最长路径

        r_len = len(matrix)
        c_len = len(matrix[0])

        for i in range(r_len):
            for j in range(c_len):
                dfs(i, j)
        return max(dp.values())

"""
你还可以使用python 自带的lru_cache 代替dp，简化后的代码如下
"""

from functools import lru_cache
# @lc code=start

class Solution_l:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # step 1 定义相关数据解构
        if not matrix:
            return 0

        @lru_cache(None)
        def dfs(r: int, c: int):
            #           上       下       左       右
            poses = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            best = 1
            for p_r, p_c in poses:
                # 未开始 & 已完结的 && value > cur_value
                n_r = r + p_r
                n_c = c + p_c
                if 0 <= n_r < r_len and 0 <= n_c < c_len and matrix[n_r][n_c] > matrix[r][c]:
                    best = max(best, dfs(n_r, n_c) + 1)
            return best

        r_len, c_len = len(matrix), len(matrix[0])
        ans = 0
        for i in range(r_len):
            for j in range(c_len):
                ans = max(ans, dfs(i, j))
        return ans


from collections import deque
class Solution_TUOPU:
    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # 拓扑排序解法
        # step1: 处理边界条件
        if not matrix:
            return 0
        r_len, c_len = len(matrix), len(matrix[0])
        outdegrees = [[0] * c_len for _ in range(r_len)]

        # step2: 初始化队列
        queue = deque()

        # step3: 计算出度
        for r in range(r_len):
            for c in range(c_len):
                for s_r, s_c in Solution.DIRS:
                    n_r = r + s_r
                    n_c = c + s_c
                    if 0 <= n_r < r_len and 0 <= n_c < c_len and matrix[n_r][n_c] > matrix[r][c]:
                        outdegrees[r][c] += 1
                if outdegrees[r][c] == 0:
                    queue.append((r, c))

        # step4: 遍历队列
        ans = 0
        while queue:
            ans += 1
            # 9 9 4
            # 6 6 8
            # 2 1 1
            #  第一层： 9 9 8
            # 第二层： 6 6 4 1
            # 第三层： 2
            # 第四层： 1
            size = len(queue)
            for _ in range(size):
                r, c = queue.popleft()
                for s_r, s_c in Solution.DIRS:
                    n_r, n_c = r + s_r, c + s_c
                    if 0 <= n_r < r_len and 0 <= n_c < c_len and matrix[n_r][n_c] < matrix[r][c]:
                        outdegrees[n_r][n_c] -= 1
                        if outdegrees[n_r][n_c] == 0:
                            queue.append((n_r, n_c))

        # step5: return
        return ans