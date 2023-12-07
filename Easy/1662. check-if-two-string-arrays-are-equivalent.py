# 1662. Check If Two String Arrays are Equivalent https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
# Runtime: 15 ms
# Memory Usage: 13.40 MB
class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        return ''.join(word1) == ''.join(word2)
