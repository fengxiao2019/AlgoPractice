253. 会议室 II
**代码**
```python
"""
解题思路：
step1: 排序，让先开会的team先占用会议室
step2: 假设现在有个会议M，M想要去看有没有空闲的会议室，需要查看M之前已经开始的会议的结束时间是否大于M会议的开始时间，如果有的话，说明有会议室空闲，否则就要新开一个会议室。
step4: 返回step2过程中统计的会议室的个数
假设用dp[i] 表示第i个会议开始后总会议室的个数
dp[0] = 1
dp[1] = x
dp[i] = max([dp[i] + 1 for i in range(j) if intervals[j][0] < intervals[i][1]], 1)
时间复杂度：O(n^2)
空间复杂度：O(n)
"""

def minMeetingRooms(intervals: List[List[int]]) -> int:
    intervals.sort()
    dp = [1] * len(intervals)
    for i in range(1, len(intervals)):
        for j in range(i):
            if intervals[j][1] > intervals[i][0]:
                dp[i] += 1
    
    return max(dp)


"""
优化：在判断我是否需要新开一个会议室时我其实只需要关心当前是否有会议结束
可以通过一个最小堆来维持当前会议室的结束时间，如果当前开始时间大于最小堆的结束时间，那就把最小堆顶部的元素弹出，压入新的元素，否则就直接压入最小堆。
时间复杂度：O(nlogn)
空间复杂度：O(n)
"""

def minMeetingRooms(intervals: List[List[int]]) -> int:
    if len(intervals) <= 1: return len(intervals)
    intervals.sort()
    heap = []
    heapq.heapify(heap)
    heapq.heappush(heap, intervals[0][1])
    for i in range(1, len(intervals)):
        if heap[0] <= intervals[i][0]:
            heapq.heappop(heap)
        heapq.heappush(heap, intervals[i][1])
    return len(heap)
```
