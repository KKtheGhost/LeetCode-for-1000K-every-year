## Write a program to solve a Sudoku puzzle by filling the empty cells.
## 
## A sudoku solution must satisfy all of the following rules:
## 
## Each of the digits 1-9 must occur exactly once in each row.
## Each of the digits 1-9 must occur exactly once in each column.
## Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
## Empty cells are indicated by the character '.'.

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def solver(i, j):
            if j > 8:  # Go to next row
                i += 1
                j = 0
            if i == 9:  # Success
                return True
            if board[i][j] != '.':  # Entry exists
                return solver(i, j+1)
                            
            # Get candidates for board[i][j]
            row = set(board[i])
            col = set(board[r][j] for r in xrange(9))
            s, t = 3*(i//3), 3*(j//3)  # Row/column starting point of block
            block = set(board[r][c] for r in xrange(s, s+3) for c in xrange(t, t+3))
            candidates = set(map(str, range(1, 10))) - (row | col | block)
            if not candidates:  # Failed
                return False
                            
            # Backtracking
            for c in candidates:
                board[i][j] = c
                if solver(i, j+1):  # Keep solving
                    return True
                board[i][j] = '.'  # Undo
            return False

        solver(0, 0)
        return