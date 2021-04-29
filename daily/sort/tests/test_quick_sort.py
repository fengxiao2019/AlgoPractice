import unittest
from daily.sort.src.quick_sort import QuickSort, QuickSort2
from daily.sort.src.bubble_sort import BubbleSort
from daily.sort.src.insert_sort import InsertSort
from daily.sort.src.bucket_sort import BucketSort
from daily.sort.src.heap_sort import HeapSort
from daily.sort.src.radix_sort import RadixSort


class BaseMixin(object):
    def test_empty(self):
        a = []
        self.qs(a)
        self.assertEqual(a, [])

    def test_one(self):
        a = [1]
        self.qs(a)
        self.assertEqual(a, [1])

    def test_two(self):
        a = [2, 1]
        self.qs(a)
        self.assertEqual(a, [1, 2])


class TestQuickSort(unittest.TestCase, BaseMixin):
    def setUp(self) -> None:
        self.qs = QuickSort()


class TestQuickSort2(unittest.TestCase, BaseMixin):
    def setUp(self) -> None:
        self.qs = QuickSort2()


class TestBubbleSort(unittest.TestCase, BaseMixin):
    def setUp(self) -> None:
        self.qs = BubbleSort()


class TestInsertSort(unittest.TestCase, BaseMixin):
    def setUp(self) -> None:
        self.qs = InsertSort()


class TestBucketSort(unittest.TestCase, BaseMixin):
    def setUp(self) -> None:
        self.qs = BucketSort()


class TestBucketSort(unittest.TestCase, BaseMixin):
    def setUp(self) -> None:
        self.qs = HeapSort()


class TestRadixSort(unittest.TestCase, BaseMixin):
    def setUp(self) -> None:
        self.qs = RadixSort()
