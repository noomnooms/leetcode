# 1732. Find the Highest Altitude https://leetcode.com/problems/find-the-highest-altitude/
# Runtime: 11 ms
# Memory: 13.23 MB
class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        maxx = 0
        alt = 0
        for i in gain:
            alt+=i
            maxx = max(maxx, alt)
        return maxx