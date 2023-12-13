# 1464. Maximum Product of Two Elements in an Array https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array
# Runtime: 25 ms
# Memory Usage: 13.30 MB
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return (nums[-1]-1)*(nums[-2]-1)
        