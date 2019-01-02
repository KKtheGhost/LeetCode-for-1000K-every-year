## Given a collection of distinct integers, return all possible permutations.
## 
## Example:
## 
## Input: [1,2,3]
## Output:
## [
##   [1,2,3],
##   [1,3,2],
##   [2,1,3],
##   [2,3,1],
##   [3,1,2],
##   [3,2,1]
## ]

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            size = len(res)
            for i in range(size):
                prev = res.pop(0)
                prev.append(num)
                for j in range(len(prev)):
                    prev[j], prev[-1] = prev[-1], prev[j]
                    res.append(prev[:])
                    prev[j], prev[-1] = prev[-1], prev[j]
        return res