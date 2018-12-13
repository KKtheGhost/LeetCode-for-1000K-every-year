## Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
## 
## Your algorithm's runtime complexity must be in the order of O(log n).
## 
## If the target is not found in the array, return [-1, -1].
## 
## Example 1:
## 
## Input: nums = [5,7,7,8,8,10], target = 8
## Output: [3,4]
## Example 2:
## 
## Input: nums = [5,7,7,8,8,10], target = 6
## Output: [-1,-1]

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r, n = 0, len(nums) - 1, len(nums)
        while l <= r:
            mid = (l+r)//2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                l = r = mid
                while l > 0 and nums[l - 1] == nums[l]:
                    l -= 1
                while r + 1 < n and nums[r + 1] == nums[r]:
                    r += 1
                return [l, r]
        return [-1, -1]