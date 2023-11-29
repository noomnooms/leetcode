# 58. Length of Last Word https://leetcode.com/problems/length-of-last-word/
# Runtime: 16 ms
# Memory Usage: 13.50 MB
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split()[-1])
