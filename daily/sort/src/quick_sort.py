class QuickSort(object):
    def __call__(self, nums):
        self._helper(nums)
    # 具体细节可以参考
    # http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/7-Sort/quick-sort1.html

    def _helper(self, nums):
        # 特殊case 处理, 边界条件真理
        if len(nums) <= 1:
            return nums
        # 选取pivot，一般选择最后一个值
        pivot = nums[-1]
        left, right = [], []
        # left 存储比pivot小的值
        # right 存储比pivot大的值
        for item in nums[:-1]:
            if item <= pivot:
                left.append(item)
            else:
                right.append(item)
        # divide
        self._helper(left)
        self._helper(right)
        # conquer, 把排序好的数据回写到nums中
        k = 0
        i = 0
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        j = 0
        nums[k] = pivot
        k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1


class QuickSort2(object):
    # 优化版本，inplace 排序
    def __call__(self, nums):
        self._helper(nums, 0, len(nums))

    def _partion(self, nums, left, right):
        right_most = right - 1
        pivot = nums[right_most]
        j = right_most - 1
        i = left
        # i, j 因为要在满足条件下进行swap，所以需要i < j, 如果i == j 置换就没有意义了
        while i <= j:
            # 我们最终要找到一个点m，m 左边的数小于pivot, 右边的数大于pivot
            if nums[j] >= pivot:
                # 把大于pivot的数调整到right_most
                nums[right_most] = nums[j]
                right_most -= 1
                j -= 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[right_most] = pivot
        return i

    def _helper(self, nums, left, right):
        # 退出递归的条件
        if right - left <= 1:
            return nums[left: right]

        # 原地拆分nums，使得pivot左边的元素小于等于pivot，
        # pivot右边的元素大于等于pivot
        mid = self._partion(nums, left, right)
        self._helper(nums, left, mid)
        self._helper(nums, mid + 1, right)
        # 因为是原地排序所以不需要合并



