# 136. Single Number https://leetcode.com/problems/single-number/
# Runtime: 92 ms
# Memory Usage: 15.53 MB
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(1, len(nums), 2):
            if nums[i] != nums[i-1]:
                return nums[i-1]
        return nums[-1]
