# 1846. Maximum Element After Decreasing and Rearranging https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/
# Runtime: 368 ms
# Memory Usage: 21.35 MB
class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        arr[0] = 1
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] > 1: arr[i] = arr[i-1]+1
        return arr[-1]