# 1266. Minimum Time Visiting All Points https://leetcode.com/problems/minimum-time-visiting-all-points/
# Runtime: 30 ms
# Memory Usage: 13.58 MB
class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        time = 0
        for i in range(1, len(points)):
            time += max(abs(points[i][0]-points[i-1][0]),
                        abs(points[i][1]-points[i-1][1]))
        return time
