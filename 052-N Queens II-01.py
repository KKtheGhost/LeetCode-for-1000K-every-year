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

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<1:
            return 0
        self.total = 0
        self.dfs(n,[],[],[])
        return self.total

    def dfs(self, nums, queens, pq_sum, pq_diff):
        p = len(queens)
        if p == nums:
            self.total += 1
            return  # backtrack
        for q in range(nums):
            if q not in queens and (p+q) not in pq_sum and (p-q) not in pq_diff:
                self.dfs(nums, queens+[q], pq_sum+[p+q], pq_diff+[p-q])