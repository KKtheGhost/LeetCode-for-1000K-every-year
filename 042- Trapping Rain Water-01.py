## Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
## 
## 
## The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
## 
## Example:
## 
## Input: [0,1,0,2,1,0,1,3,2,1,2,1]
## Output: 6

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        l, r, amount, minHeight = 0, n - 1, 0, 0
        while l < r:
            while l < r and height[l] <= minHeight:
                amount += minHeight - height[l]
                l += 1
            while r > l and height[r] <= minHeight:
                amount += minHeight - height[r]
                r -= 1
            minHeight = min(height[l], height[r])
        return amount