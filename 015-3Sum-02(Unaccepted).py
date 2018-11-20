## Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
## 
## Note:
## 
## The solution set must not contain duplicate triplets.
## 
## Example:
## 
## Given array nums = [-1, 0, 1, 2, -1, -4],
## 
## A solution set is:
## [
##   [-1, 0, 1],
##   [-1, -1, 2]
## ]

##超时答案，通过不了Submit。复杂度是O(N^2logn)
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        result,arr = [],[]
        while 3 <= len(nums):
            j,t = 0,nums[0]
            del nums[0]
            while j < len(nums):
                numt = list(nums)
                s = numt[j]
                del numt[j]
                if -t-s in numt:
                    arr = [t,s,-t-s]
                    arr.sort()
                if arr not in result and arr != []:
                    result.append(arr)
                j += 1
        return result