# 2352. Equal Row and Column Pairs https://leetcode.com/problems/equal-row-and-column-pairs/
# Runtime: 473 ms
# Memory: 17.35 MB
class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0 
        for j in range(len(grid)):
            column = []
            for row in grid:
                column.append(row[j])
            ans += grid.count(column)
            
        return ans 