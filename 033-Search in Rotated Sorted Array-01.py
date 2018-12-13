## Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
## 
## (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
## 
## You are given a target value to search. If found in the array return its index, otherwise return -1.
## 
## You may assume no duplicate exists in the array.
## 
## Your algorithm's runtime complexity must be in the order of O(log n).
## 
## Example 1:
## 
## Input: nums = [4,5,6,7,0,1,2], target = 0
## Output: 4
## Example 2:
## 
## Input: nums = [4,5,6,7,0,1,2], target = 3
## Output: -1

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        N=n=len(nums)
        if not nums:
            return -1
        if target <= nums[N-1]:
            while n > -1:
                if target == nums[n-1]:
                    return n-1
                else:
                    n -= 1
        else:
            n = 0
            while n < N:
                if target == nums[n]:
                    return n
                else:
                    n += 1
        return -1