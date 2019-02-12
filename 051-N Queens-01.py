## The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
##
## Given an integer n, return all distinct solutions to the n-queens puzzle.
## 
## Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
## 
## Example:
## 
## Input: 4
## Output: [
##  [".Q..",  // Solution 1
##   "...Q",
##   "Q...",
##   "..Q."],
## 
##  ["..Q.",  // Solution 2
##   "Q...",
##   "...Q",
##   ".Q.."]
## ]
## Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def DFS(queens, xy_dif, xy_sum):
            p = len(queens)
            if p==n:
                result.append(queens)
                return None
            for q in range(n):
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
                    DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])  
        result = []
        DFS([],[],[])
        return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]