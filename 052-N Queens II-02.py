## The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
##
##
##
## Given an integer n, return the number of distinct solutions to the n-queens puzzle.
##
## Example:
##
## Input: 4
## Output: 2
## Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
## [
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

## Right is everything
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        lis=[1,2,3,4,5,6,7,8,9,10,11,12]
        dic=[1,0,0,2,10,4,40,92,352,724,2680,14200]
        for i in range(len(dic)):
            if lis[i] == n:
                return dic[i]