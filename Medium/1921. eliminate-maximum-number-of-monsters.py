# 1921. Eliminate Maximum Number of Monsters https://leetcode.com/problems/eliminate-maximum-number-of-monsters/
# Runtime: 672 ms
# Memory Usage: 24.96 MB
class Solution(object):
    def eliminateMaximum(self, dist, speed):
        """
        :type dist: List[int]
        :type speed: List[int]
        :rtype: int
        """
        for i in range(len(dist)):
            dist[i] = int(ceil(dist[i]/float(speed[i])))
            speed[i] = 0

        for i in range(len(dist)):
            if dist[i] < len(dist): 
                speed[dist[i]] += 1
        
        sum = 0
        for i in range(len(speed)):
            sum += speed[i]
            if sum >= i+1: return i
        return len(speed)