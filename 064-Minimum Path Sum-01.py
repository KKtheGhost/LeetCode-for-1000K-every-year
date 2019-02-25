## Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
## 
## Note: You can only move either down or right at any point in time.
## 
## Example:
## 
## Input:
## [
##   [1,3,1],
##   [1,5,1],
##   [4,2,1]
## ]
## Output: 7
## Explanation: Because the path 1→3→1→1→1 minimizes the sum.

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])          #m代表矩阵的高度，n代表矩阵的宽度，是一个n*m的矩阵
        dp=[[float('inf') for _ in range(n + 1)] for _ in range(m + 1)]     # float('inf')代表正负无穷区间
        dp[1][1] = grid[0][0]       ##声明dp开启位置
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i + j == 2:  continue
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i - 1][j - 1]
        return dp[m][n]
