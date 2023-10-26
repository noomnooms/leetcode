# 1. Two Sum https://leetcode.com/problems/two-sum/
# Runtime: 4112 ms
# Memory Usage: 14.9 MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]