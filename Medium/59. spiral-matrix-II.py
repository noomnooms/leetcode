# 59. Spiral Matrix II https://leetcode.com/problems/spiral-matrix-ii/
# Runtime: 14 ms
# Memory Usage: 13.35 MB
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for i in range(n)] for j in range(n)]

        start_row, start_col, end_row, end_col = 1, 0, n-1, n-1
        row, col = 0, 0
        dir = 'right'
        for i in range(1, (n*n)+1):
            matrix[row][col] = i

            if dir == 'right':
                if col+1 <= end_col:
                    col += 1
                else:
                    end_col -= 1
                    row += 1
                    dir = 'down'

            elif dir == 'down':
                if row+1 <= end_row:
                    row += 1
                else:
                    end_row -= 1
                    col -= 1
                    dir = 'left'

            elif dir == 'left':
                if col-1 >= start_col:
                    col -= 1
                else:
                    start_col += 1
                    row -= 1
                    dir = 'up'

            elif dir == 'up':
                if row-1 >= start_row:
                    row -= 1
                else:
                    start_row += 1
                    col += 1
                    dir = 'right'

        return matrix
