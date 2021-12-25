from typing import List
import collections
import heapq

"""
利用桶排序的思想
先获取最多的出现次数，假设为max_count，桶的个数就为max_count + 1(下标从0开始)
将出现次数相同的元素放入到对应的桶中（出现的次数就是桶的下标）
因为要求返回的结果集中，如果出现次数相同，按照字典序进行排序，所以，需要对桶中的元素进行排序
对桶列表按照逆序排序，遍历每个桶的元素并加入到结果集中，直到满足退出条件

边界条件：如果元素的数量小于k，那么直接返回排序好的words
时间复杂度：O(n)
空间复杂度：O(n)
"""
def topKFrequent(words: List[str], k: int) -> List[int]:
    if len(words) <= k:
        words.sort()
        return words

    counter = collections.Counter(words)
    max_count = max(counter.values()) + 1
    buckets = [[] for i in range(max_count)]

    for key, v in counter.items():
        buckets[v].append(key)
    res = []
    for bucket in buckets[::-1]:
        bucket.sort()
        for word in bucket:
            if len(res) >= k:
                return res
            else:
                res.append(word)
    return res

"""
堆排序
时间复杂度：O(nlogn)
空间复杂度：O(n)
"""
def topKFrequent(words: List[str], k: int) -> List[str]:
    counter = collections.Counter(words)
    heap = []
    for key, v in counter.items():
        heapq.heappush(heap, (v, key))

    res = []
    while heap:
        res.append(heapq.heappop(heap))
    sorted_res = sorted(res, key=lambda x: (~x[0], x[1]))
    res = []
    for item in sorted_res:
        res.append(item[1])
    return res[:k]