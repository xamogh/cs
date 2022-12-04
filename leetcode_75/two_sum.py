from typing import List
import unittest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}  # number => index
        for idx, num in enumerate(nums):
            target_key = target - num
            if target_key in map:
                return [idx, map[target_key]]
            else:
                map[num] = idx
        return []


class test_two_sum(unittest.TestCase):
    def test_two_sum_success(self):
        r = Solution()
        self.assertEqual(r.two_sum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(r.two_sum([3, 2, 4], 6), [1, 2])
        self.assertEqual(r.twoSum)
