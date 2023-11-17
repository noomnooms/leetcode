# 1980. Find Unique Binary String https://leetcode.com/problems/find-unique-binary-string/
# Runtime: 9 ms
# Memory Usage: 13.17 MB
class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        nums.sort()
        lenstr = len(nums[0])
        curr = 0
        unique = "{0:b}".format(curr).rjust(lenstr, '0')
        for i in nums:
            if i == unique: 
                curr += 1
                unique = "{0:b}".format(curr).rjust(lenstr, '0')
            else: return unique
        return unique
        