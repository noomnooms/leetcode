# 35. Search Insert Position https://leetcode.com/problems/search-insert-position
# Runtime: 28 ms
# Memory Usage: 13.9 MB
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            # print(target, nums[i])
            if nums[i] > target:
                return i
            if nums[i] == target:
                return i
        return len(nums)
