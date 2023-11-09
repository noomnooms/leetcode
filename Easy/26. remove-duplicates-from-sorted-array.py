# 26. Remove Duplicates from Sorted Array https://leetcode.com/problems/remove-duplicates-from-sorted-array
# Runtime: 59 ms
# Memory Usage: 14.61 MB
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = list({i for i in nums})
        a.sort()
        for i in range(len(a)):
            nums[i] = a[i]
        return len(a)
        