## Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
##
## Example 1:
##
## Input:
## [
##  [ 1, 2, 3 ],
##  [ 4, 5, 6 ],
##  [ 7, 8, 9 ]
## ]
## Output: [1,2,3,6,9,8,7,4,5]
## Example 2:
##
## Input:
## [
##   [1, 2, 3, 4],
##   [5, 6, 7, 8],
##   [9,10,11,12]
## ]
## Output: [1,2,3,4,8,12,11,10,9,5,6,7]

## This idea is from Python God StafanPochmann.
## Taking matrix[0] away, and rotating the matrix 90 degree.
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        return matrix and list(matrix.pop(0)) + self.spiralOrder(zip(*matrix)[::-1])