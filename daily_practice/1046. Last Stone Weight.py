"""
用stones 构建小顶堆
[-1, -1, -2, -4, -7, -8]
每次从堆里弹出两个元素：
第一次： -8 -7 => -8 != -7 => -1 => [-1, -1, -1, -2, -4]
第二次：-4 -2 => -4 != -2 => -2 => [-1, -1, -1, -2]
第三次：-2 -1 => -2 != -1 => -1 => [-1, -1, -1]
第四次： -1 -1 => -1 == -1 => 0 => [-1] 队列中的元素数量小于2个了，退出

如果队列中还有元素：返回队列中的元素
否则 返回0
时间复杂度：O(nlogn)
空间复杂度：O(n)
"""
from typing import List
import heapq

def lastStoneWeight(stones: List[int]) -> int:
    heap = []
    heapq.heapify(heap)
    for item in stones:
        heapq.heappush(heap, -item)

    while len(heap) > 1:
        stone1 = heapq.heappop(heap)
        stone2 = heapq.heappop(heap)
        if stone1 != stone2:
            heapq.heappush(heap, stone1 - stone2)
    if heap:
        res = heapq.heappop(heap)
        return -res
    return 0