# 1502. Can Make Arithmetic Progression From Sequence https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/
# Runtime: 15 ms
# Memory Usage: 13.12 MB
class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        diff = arr[1]-arr[0]
        for i in range(2, len(arr)):
            if arr[i]-arr[i-1] != diff:
                return False
        return True
