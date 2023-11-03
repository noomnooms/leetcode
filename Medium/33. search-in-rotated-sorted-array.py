# 33. Search in Rotated Sorted Array https://leetcode.com/problems/search-in-rotated-sorted-array/
# Runtime: 15 ms
# Memory Usage: 13.51 MB
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans = -1
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return ans
