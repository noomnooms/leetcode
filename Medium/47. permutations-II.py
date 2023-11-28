# 47. Permutations II https://leetcode.com/problems/permutations-ii/
# Runtime: 440 ms
# Memory Usage: 18.92 MB
import itertools


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        for el in list(itertools.permutations(nums)):
            if el not in ans:
                ans.append(el)
        return ans
