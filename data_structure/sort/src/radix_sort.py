class RadixSort(object):
    """
    基数排序
    基数排序的时间复杂度：O(n)
    """
    def __call__(self, nums):
        self._helper(nums)

    def _helper(self, nums):
        if len(nums) <= 1:
            return
        max_v = max(nums)
        exp = 1
        while max_v // exp > 0:
            self._count_sort(nums, exp)
            exp = exp * 10

    def _count_sort(self, nums, exp):
        count = [0] * 10
        # exp 10进制表示法；
        # 个位上的数exp = 1
        # 十位上的数exp = 10
        # ....
        for i in range(len(nums)):
            index = nums[i] // exp
            count[index % 10] += 1

        # 累加，累加完就能算出来每个元素最右边+1的位置
        # 例如count[5] = 4
        # 那么5 在数组中的位置位4-1=3
        for i in range(1, 10):
            count[i] += count[i - 1]

        # 输出按照个位或其它位上排好序的数
        output = [0] * len(nums)
        for item in nums:
            index = item//exp
            # 下面两行代码很有技巧
            output[count[index % 10] - 1] = item
            # 因为有重复元素，所以，减去1，记录下一个该元素应该存储的位置
            count[index % 10] -= 1

        for i in range(len(output)):
            nums[i] = output[i]