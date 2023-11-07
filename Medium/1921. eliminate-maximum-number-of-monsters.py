# 1921. Eliminate Maximum Number of Monsters https://leetcode.com/problems/eliminate-maximum-number-of-monsters/
# Runtime: 837 ms
# Memory Usage: 36.6 MB
class Solution(object):
    def eliminateMaximum(self, dist, speed):
        """
        :type dist: List[int]
        :type speed: List[int]
        :rtype: int
        """
        arrival = []
        for i in range(len(dist)):
            arrival.append([dist[i]/float(speed[i]), i])
        arrival.sort()
        
        t = 0
        cnt = 0

        while cnt<len(dist):
            posi = dist[arrival[cnt][1]] - (speed[arrival[cnt][1]]*t)
            if posi>0: cnt += 1
            else: break
            t+= 1
        return cnt