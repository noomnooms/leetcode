# 37. Sudoku Solver https://leetcode.com/problems/sudoku-solver/
# Runtime: 116 ms
# Memory Usage: 13.21 MB
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row = [[] for i in range(9)]
        col = [[] for i in range(9)]
        box = [[[] for i in range(3)] for j in range(3)]

        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    row[i].append(board[i][j])
                    col[j].append(board[i][j])
                    box[i//3][j//3].append(board[i][j])

        def backtrack (r, c):
            if board[r][c] != '.':
                if c+1<9: return backtrack(r, c+1)
                elif r+1<9: return backtrack(r+1, 0)
                else: return True 
            else:
                for i in range(1, 10):
                    str_i = str(i)
                    if str_i not in row[r] and str_i not in col[c] and str_i not in box[r//3][c//3]:
                        row[r].append(str_i)
                        col[c].append(str_i)
                        box[r//3][c//3].append(str_i)

                        if c+1<9: res = backtrack(r, c+1)
                        elif r+1<9: res = backtrack(r+1, 0)
                        else: res = True

                        if (res): 
                            board[r][c] = str_i
                            return True
                        else: 
                            row[r].pop()
                            col[c].pop()
                            box[r//3][c//3].pop()
                return False
                
        backtrack(0, 0)