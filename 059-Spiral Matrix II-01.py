## Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
##
## Example:
##
## Input: 3
## Output:
## [
##  [ 1, 2, 3 ],
##  [ 8, 9, 4 ],
##  [ 7, 6, 5 ]
## ]

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res, lo = [], n*n+1
        while lo > 1:
            lo, hi = lo - len(res), lo
            res = [range(lo, hi)] + zip(*res[::-1])
        return res