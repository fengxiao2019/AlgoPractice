
# %%
from numpy import random


class BUMS(object):
    def __init__(self, values):
        self.values = values

    def sort_t(self, sts, end):
        if end - sts <= 1:
            return self.values[sts:end]
        mid = (sts + end) // 2
        left = self.sort_t(sts, mid)
        right = self.sort_t(mid, end)
        return self.merge(left, right)

    def sort_bu(self):
        # http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/7-Sort/merge-sort5.html
        # first loop: a[0:2] a[2:4] a[4:6] a[6:8]
        # width = 1, first loop turned into : 
        # a[0*width, 2*width], a[2*width, 4*width], a[4*width, 6*width], a[6*width, 8*width]
        # second loop: a[0:4] a[4:8]
        # width = 2, second loop turned into:
        # a[0*width, 2*width], a[2*width, 4*width]
        # third loop: a[0:8]
        # width = 4, third loop turn into:
        # a[0*width, 2*width]
        # so in the outer loop we can control the width's increment, the increment step
        # is step = 2*width
        # in the inner loop, we split the array into small parts, then use the merge function

        width = 1
        arr_len = len(self.values)
        while width < arr_len:
            i = 0
            while i + 2 * width < arr_len:
                self.merge_inplace(self.values, i, i + width, i + 2 * width)
                i += 2 * width
            width *= 2
        return self.values

    @staticmethod
    def merge_inplace(values, start, mid, end):
        tmp = []
        i, j = start, mid
        print(f"len: {len(values)}, start: {start}, end:{end}")
        while i < mid and j < end:
            print(f"i: {i}, j: {j}")
            if values[i] < values[j]:
                tmp.append(values[i])
                i += 1
            else:
                tmp.append(values[j])
                j += 1
            
        if i < mid:
            tmp.extend(values[i:mid])
        if j < end:
            tmp.extend(values[j:end])
        return tmp
        for i in range(end - start):
            values[start + i] = tmp[i]

    @staticmethod
    def merge(left, right):
        tmp = []
        len_l = len(left)
        len_r = len(right)
        i = 0
        j = 0
        while i < len_l and j < len_r:
            if left[i] <= right[j]:
                tmp.append(left[i])
                i += 1
            else:
                tmp.append(right[j])
                j += 1

        if i < len_l:
            tmp.extend(left[i:])
        if j < len_r:
            tmp.extend(right[j:])
        return tmp


class MSortedArray(object):

    @classmethod
    def solution(cls, arr1, arr2):
        tmp = []
        arr1_len = len(arr1)
        arr2_len = len(arr2)
        i, j = 0, 0
        while i < arr1_len or j < arr2_len:
            if i < arr1_len and j < arr2_len:
                if arr1[i] <= arr2[j]:
                    tmp.append(arr1[i])
                    i += 1
                else:
                    tmp.append(arr2[j])
                    j += 1
            elif i < arr1_len:
                tmp.extend(arr1[i:])
                break
            elif j < arr2_len:
                tmp.extend(arr2[j:])
                break
        return tmp

    @classmethod
    def solution_1(cls, arr1, arr2):
        tmp = []
        arr1_len = len(arr1)
        arr2_len = len(arr2)
        i, j = 0, 0
        while i < arr1_len and j < arr2_len:
            if arr1[i] <= arr2[j]:
                tmp.append(arr1[i])
                i += 1
            else:
                tmp.append(arr2[j])
                j += 1
        
        if i < arr1_len:
            tmp.extend(arr1[i:])
        if j < arr1_len:
            tmp.extend(arr2[j:])
        return tmp


def test_1():
    s = BUMS(random.randint(100000, size=100))
    res = BUMS.sort_t(s.values, 0, len(s.values))
    print(res)


def test_sorted_array():
    arr1 = random.randint(10, size=10)
    arr2 = random.randint(30, size=10)
    s1 = sorted(arr1)
    s2 = sorted(arr2)
    res = MSortedArray.solution(s1, s2)
    res1 = MSortedArray.solution_1(s1, s2)
    bums1 = BUMS(s1)
    assert bums1.sort_t(0, len(bums1.values)) == s1
    bums2 = BUMS(s2)
    assert bums2.sort_t(0, len(bums2.values)) == s2
    print(res)
    print(res1)
    res = bums1.sort_bu()
    print(f'bu_sort: \n{res}\nres:\n{s1}')
    assert res == s1 


test_sorted_array()
# %%
from numpy import random


class InsertSort(object):
    """
    http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/7-Sort/insertion-sort.html
    """
    def __init__(self, values):
        self.values = values
    
    def execute(self):
        index = 0
        length = len(self.values)
        if length <= 1:
            return self.values

        values = self.values
        while index < length:
            min_value = values[index]
            min_index = index
            # 从剩下的牌中找出最小的, 记录下最小牌所在的index
            for i, v in enumerate(self.values[index:]):
                if v < min_value:
                    # 注意这里要加上index
                    min_index = i + index
                    min_value = v
            # 把最小的牌插到未整理的牌最开始的位置
            values[index], values[min_index] = values[min_index], values[index]
            index += 1
        self.values = values
        return values


def test_insert_sort():
    arr1 = random.randint(100, size=20)
    s1 = sorted(arr1)
    res = InsertSort(list(arr1)).execute()
    assert res == s1


test_insert_sort()

# %%
from numpy import random


class QS(object):
    """
    http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/7-Sort/quick-sort2.html#partition
    """
    def __init__(self, values):
        self.values = values

    def sort(self):
        self._execute(0, len(self.values))
        return self.values

    def _execute(self, left, right):
        if right - left <= 1:
            return
        mid = self.partition(left, right)
        self._execute(left, mid)
        self._execute(mid, right)

    def partition(self, left, right):
        pivot = self.values[right - 1]
        large_i = right - 1
        small_i = left
        while small_i < large_i:
            if self.values[large_i - 1] > pivot:
                self.values[large_i] = self.values[large_i - 1]
                large_i -= 1
            else:
                print(len(self.values), large_i - 1, small_i)
                self.values[large_i - 1], self.values[small_i] = self.values[small_i], self.values[large_i - 1]
                small_i += 1
        self.values[large_i] = pivot
        return large_i


def test():
    arr1 = random.randint(100, size=20)
    s1 = sorted(arr1)
    res = QS(list(arr1)).sort()
    print(res)
    print(s1)
    assert res == s1