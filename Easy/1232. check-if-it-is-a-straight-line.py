# 1232. Check If It Is a Straight Line https://leetcode.com/problems/check-if-it-is-a-straight-line/
# Runtime: 43 ms
# Memory Usage: 13.57 MB
class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        y = (coordinates[1][1]-coordinates[0][1])
        x = (coordinates[1][0]-coordinates[0][0])

        for i in range(2, len(coordinates)):
            y_tmp = coordinates[i][1]-coordinates[i-1][1]
            x_tmp = coordinates[i][0]-coordinates[i-1][0]
            if (y==0 and y_tmp!=0) or (x==0 and x_tmp!=0) or (x_tmp!=0 and y_tmp/x_tmp != y/x) or (x_tmp==0 and x!=0): 
                return False
            
        return True
        