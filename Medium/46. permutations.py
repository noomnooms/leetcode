# 46. Permutations https://leetcode.com/problems/permutations/
# Runtime: 7ms
# Memory Usage: 13.40 MB
import itertools


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return list(itertools.permutations(nums))
