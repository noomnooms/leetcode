# 54. Spiral Matrix https://leetcode.com/problems/spiral-matrix/
# Runtime: 17 ms
# Memory Usage: 13.40 MB
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        start_row, start_col, end_row, end_col = 1, 0, len(matrix)-1, len(matrix[0])-1
        row, col = 0, 0
        dir = 'right'

        for i in range((len(matrix)*len(matrix[0]))):
            ans.append(matrix[row][col])

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
        return ans
        