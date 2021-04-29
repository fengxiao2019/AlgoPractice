from typing import List
import math
# Bucket sort is mainly useful
# when input is uniformly distributed over a range.


class BucketSort(object):
    def __call__(self, nums: List[int]) -> None:
        self._helper(nums, 10)

    def _helper(self, nums: List[int], k) -> None:
        if len(nums) <= 1:
            return nums
        buckets = [[] for _ in range(k)]
        max_value = max(nums)

        # 将数据插入到不同的桶中
        for item in nums:
            index = math.floor(k * item / max_value)
            index = min(index, k - 1)
            print(index)
            buckets[index].append(item)

        # 对bucket内的数据进行排序
        for item in buckets:
            item.sort()
        k = 0
        print(buckets)
        for bucket in buckets:
            if not buckets:
                continue
            for i in range(len(bucket)):
                nums[k] = bucket[i]
                k += 1
        print(nums)


def test(data):
    bs = BucketSort()
    bs(data)
print(test([3, 1, 9, 4, 7, 12]))
