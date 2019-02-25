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

dp = [[0] * len(grid[0]) for _ in xrange(len(grid))]
    for i in xrange(len(grid)):
        for j in xrange(len(grid[0])):
            dp[i][j] = (0 if not i + j else min(dp[i][j - 1] if j > 0 else float('inf'), dp[i - 1][j] if i > 0 else float('inf'))) + grid[i][j]
    return dp[len(grid) - 1][len(grid[0]) - 1]
