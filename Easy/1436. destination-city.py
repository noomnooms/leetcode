# 1436. Destination City https://leetcode.com/problems/destination-city/
# Runtime: 32 ms
# Memory Usage: 13.26 MB
class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        source = [i[0] for i in paths]
        for i in paths:
            if i[1] not in source:
                return i[1]
