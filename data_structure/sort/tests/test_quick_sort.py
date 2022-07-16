import unittest
from DataStructure.sort.src import QuickSort, QuickSort2
from DataStructure.sort.src.bubble_sort import BubbleSort
from DataStructure.sort.src import InsertSort
from DataStructure.sort.src import BucketSort
from DataStructure.sort.src import HeapSort
from DataStructure.sort.src import RadixSort


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
