import bisect

# 可以利用PatienceSort 寻找最大上升子序列

class PatienceSort(object):

    def __call__(self, nums):
        return self._helper(nums)

    def _helper(self, nums):
        dp = []
        for item in nums:
            index = bisect.bisect_left(dp, item)
            if index == len(dp):
                dp.append(item)
            else:
                dp[index] = item
            yield item, index


ps = PatienceSort()
for item in ps([1, 3, 8, 2, 4]):
    print(item, end='\t')


# 输出结果
# (1, 0)  (3, 1)  (8, 2)  (2, 1)  (4, 2)