## Given a collection of numbers that might contain duplicates, return all possible unique permutations.
## 
## Example:
## 
## Input: [1,1,2]
## Output:
## [
##   [1,1,2],
##   [1,2,1],
##   [2,1,1]
## ]

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                for i in xrange(len(l)+1):
                    new_ans.append(l[:i]+[n]+l[i:])
                    if i<len(l) and l[i]==n: break
            ans = new_ans
        return ans