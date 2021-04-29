import math
from typing import List
import unittest
import random


class BSTest(unittest.TestCase):
    def setUp(self) -> None:
        self.array = random.sample(range(1000), k=10)

    def test_empty(self):
        self.assertEqual(binary_search([], 0), -1)

    def test_one(self):
        self.assertEqual(binary_search([1], 1), 0)

    def test_first_element(self):
        self.assertEqual(binary_search([1, 2, 4], 1), 0)

    def test_random_element(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6], 2), 1)

    def test_last_element(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6], 6), 5)

    def test_not_exists(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6], 10), -1)


def binary_search(nums: List[int], target: int) -> int:
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1
# """
# select distinct cert.emp_id from cm_log cl
# inner join
#    (
#       select emp.id as emp_id, emp_cert.id as cert_id from employee emp
#       left join emp_certificate emp_cert on emp.id = emp_cert.emp_id
#       where emp.is_deleted=0 ) cert
#       on ( cl.ref_table='Employee' and cl.ref_oid= cert.emp_id )
#       or ( cl.ref_table='EmpCertificate' and cl.ref_oid= cert.cert_id )
# where
#    cl.last_upd_date >='2013-11-07 15:03:00'
#    and cl.last_upd_date<='2013-11-08 16:00:00';
# """
"""
找最左或者最右, 左闭右开区间
返回的结果集中，nums[:index] < target
"""
def binary_search_left(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if target > nums[mid]:
            left = mid + 1
        else:
            # mid 此时有可能等于target 为什么还要选择开区间？不会漏掉相等的value吗？
            right = mid
    return left


"""
target >= nums[mid] => left <= mid + 1
所以返回的结果集中 nums[:index] < target 
"""
def binary_search_right(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)

    while left < right:
        mid = (left + right) // 2
        if target < nums[mid]:
            # right 是闭区间
            right = mid
        else:
            left = mid + 1
    return left
arr = [1, 2,  4, 4,4 ,5]
print(binary_search_left(arr, 3))