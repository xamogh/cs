from typing import List
import unittest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums) - 1):
            for j in range(1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


class test_two_sum(unittest.TestCase):
    def test_two_sum_success(self):
        r = Solution()
        self.assertEqual(r.two_sum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(r.two_sum([3, 2, 4], 6), [1, 2])
        self.assertEqual(r.twoSum)
