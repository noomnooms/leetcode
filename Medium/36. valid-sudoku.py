# 36. Valid Sudoku
# Runtime: 50 ms
# Memory: 13.29 MB
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [[] for i in range(9)]
        col = [[] for i in range(9)]
        box = [[[] for i in range(3)] for i in range(3)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in box[i//3][j//3]:
                        return False
                    row[i].append(board[i][j])
                    col[j].append(board[i][j])
                    box[i//3][j//3].append(board[i][j])

        return True
