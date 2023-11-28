# 2147. Number of Ways to Divide a Long Corridor https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/
# Runtime: 770 ms
# Memory Usage: 25.52 MB
class Solution(object):
    def numberOfWays(self, corridor):
        """
        :type corridor: str
        :rtype: int
        """
        if corridor.count('S') % 2 == 1 or corridor.count('S') == 0:
            return 0

        sofas = [[]]
        for i in range(len(corridor)):
            if corridor[i] == 'S':
                if len(sofas[-1]) < 2:
                    sofas[-1].append(i)
                else:
                    sofas.append([i])

        count = 1
        for i in range(1, len(sofas)):
            count *= sofas[i][0]-sofas[i-1][1]
        return count % (10**9+7)
