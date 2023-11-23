# 1424. Diagonal Traverse II https://leetcode.com/problems/diagonal-traverse-ii/
# Runtime: 682 ms
# Memory Usage: 38.73 MB
class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        for row in range(len(nums)):
            for col in range(len(nums[row])):
                if len(ans) == row+col:
                    ans.append([])
                ans[row+col].insert(0, nums[row][col])
        return [item for sublist in ans for item in sublist]
