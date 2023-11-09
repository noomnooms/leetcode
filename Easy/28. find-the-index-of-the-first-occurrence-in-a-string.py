# 28. Find the Index of the First Occurrence in a String https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# Runtime: 8 ms
# Memory Usage: 13.34 MB
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(needle)
        haystack += '$'
        for i in range(len(haystack)-n):
            if haystack[i:i+n] == needle:
                return i
        return -1
