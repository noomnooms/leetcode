# 2849. Determine if a Cell Is Reachable at a Given Time https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/
# Runtime: 12 ms
# Memory Usage: 13.08 MB
class Solution(object):
    def isReachableAtTime(self, sx, sy, fx, fy, t):
        """
        :type sx: int
        :type sy: int
        :type fx: int
        :type fy: int
        :type t: int
        :rtype: bool
        """
        maxx = max(abs(fy-sy), abs(fx-sx))
        if t < maxx or (maxx == 0 and t == 1):
            return False
        return True
