## A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
## 
## The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
## 
## Now consider if some obstacles are added to the grids. How many unique paths would there be?
## 
## 
## 
## An obstacle and empty space is marked as 1 and 0 respectively in the grid.
## 
## Note: m and n will be at most 100.
## 
## Example 1:
## 
## Input:
## [
##   [0,0,0],
##   [0,1,0],
##   [0,0,0]
## ]
## Output: 2
## Explanation:
## There is one obstacle in the middle of the 3x3 grid above.
## There are two ways to reach the bottom-right corner:
## 1. Right -> Right -> Down -> Down
## 2. Down -> Down -> Right -> Right

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return
        r, c = len(obstacleGrid), len(obstacleGrid[0])
        cur = [0] * c
        cur[0] = 1 - obstacleGrid[0][0]
        for i in xrange(1, c):
            cur[i] = cur[i-1] * (1 - obstacleGrid[0][i])
        for i in xrange(1, r):
            cur[0] *= (1 - obstacleGrid[i][0])
            for j in xrange(1, c):
                cur[j] = (cur[j-1] + cur[j]) * (1 - obstacleGrid[i][j])
        return cur[-1]
