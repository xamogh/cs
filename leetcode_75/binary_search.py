import pdb
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, target, len(nums) - 1, 0)

    def binarySearch(self, nums, target, hi, lo) -> int:
        mid = (hi + lo)//2
        if lo > hi:
            return - 1
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            return self.binarySearch(nums, target, mid - 1, lo)
        else:
            return self.binarySearch(nums, target, hi, mid+1)


r = Solution()
print(r.search([-1, 0, 3, 5, 9, 12], 9))
