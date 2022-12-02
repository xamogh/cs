from typing import List
import unittest

class Solution:
    # brute forcea n^2, 1
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(0, len(nums) - 1):
    #        for j in range(1, len(nums)):
    #            if nums[i] + nums[j] == target and i != j:
    #                return [i, j]
    #     return []

    # hash map 2 loops n + n, n
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     # loop once, make a map [number]: idx
    #     # loop again, check if its pair(target - num) exists in map
    #     map = {}
    #     for idx, num in enumerate(nums):
    #         map[num] = idx
    #     print(map)
    #     for idx, num in enumerate(nums):
    #         if (target - num) in map and idx != map[target - num]:
    #             return [idx, map[target - num]]
    #     return []
        
    # hasmap one loop n, n
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {} # number => index
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
        self.assertEqual(r.twoSum([2,7,11,15], 9).sort(), [0, 1].sort())  
        self.assertEqual(r.twoSum([3, 2, 4], 6).sort(), [1, 2].sort())  
        self.assertEqual(r.twoSum([2, 5, 5, 11], 10).sort(), [1, 2].sort())  
    
