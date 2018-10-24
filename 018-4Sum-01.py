## Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
## 
## Note:
## 
## The solution set must not contain duplicate quadruplets.
## 
## Example:
## 
## Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
## 
## A solution set is:
## [
##   [-1,  0, 0, 1],
##   [-2, -1, 1, 2],
##   [-2,  0, 0, 2]
## ]

##基本雷同3Sum，不赘述
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        arr = []                                                
        nums.sort()                                             
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:continue
            for j in range(i+1,len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:continue
                l, r = j+1, len(nums)-1 
                while l < r:                                        
                    s = nums[i] + nums[j] + nums[l] + nums[r]                 
                    if s < target:                                       
                        l +=1 
                    elif s > target:                                     
                        r -= 1
                    else:
                        arr.append((nums[i],nums[j],nums[l],nums[r]))     
                        while l < r and nums[l] == nums[l+1]:   
                            l += 1
                        while l < r and nums[r] == nums[r-1]:       
                            r -= 1
                        l += 1; r -= 1                              
        return arr