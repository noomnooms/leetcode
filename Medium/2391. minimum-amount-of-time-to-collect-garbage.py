# 2391. Minimum Amount of Time to Collect Garbage https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage
# Runtime: 651 ms
# Memory Usage: 45.66 MB
class Solution(object):
    def garbageCollection(self, garbage, travel):
        """
        :type garbage: List[str]
        :type travel: List[int]
        :rtype: int
        """
        time = 0
        metal, paper, glass = 0, 0, 0
        for i in range(len(garbage)):
            time += len(garbage[i])
            if 'M' in garbage[i]: metal = i
            if 'P' in garbage[i]: paper = i
            if 'G' in garbage[i]: glass = i 
        return time+sum([travel[i] for i in range(metal)])+sum([travel[i] for i in range(paper)])+sum([travel[i] for i in range(glass)])    

