# 1877. Minimize Maximum Pair Sum in Array https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/
# Runtime: 955 ms
# Memory Usage: 25.81 MB
class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ans = 0
        for i in range(len(nums)/2):
            ans = max(ans, nums[i]+nums[len(nums)-1-i])
        return ans