# 34. Find First and Last Position of Element in Sorted Array https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Runtime: 54 ms
# Memory Usage: 14.82 MB
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = -1
        end = -1
        for i in range(len(nums)):
            if nums[i] == target:
                if start==-1: start = i
                end = i
        return [start, end]