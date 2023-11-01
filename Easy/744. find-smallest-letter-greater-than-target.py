# 744. Find Smallest Letter Greater Than Target https://leetcode.com/problems/find-smallest-letter-greater-than-target
# Runtime: 66 ms
# Memory Usage: 15.16 MB
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for i in letters:
            if i>target: return i
        return letters[0]