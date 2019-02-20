## A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
## 
## The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
## 
## How many possible unique paths are there?
## 
## 
## Above is a 7 x 3 grid. How many possible unique paths are there?
## 
## Note: m and n will be at most 100.
## 
## Example 1:
## 
## Input: m = 3, n = 2
## Output: 3
## Explanation:
## From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
## 1. Right -> Right -> Down
## 2. Right -> Down -> Right
## 3. Down -> Right -> Right

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ##实际上就是一个排列组合
        ##可以看做Right是1，Down是0
        ##就相当于一个元组中，有m-1个1，n-1个0
        ##求最大排列组合数
        return 1 if m == 1 or n == 1 else (reduce(lambda x,y:x*y,range(1,m+n-1)))/((reduce(lambda x,y:x*y,range(1,n)))*(reduce(lambda x,y:x*y,range(1,m))))
