## Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
## 
## Note: You may not slant the container and n is at least 2.
##  ^
## 9|
## 8|  █         █
## 7|  █         █   █
## 6|  █ █       █   █
## 5|  █ █   █   █   █
## 4|  █ █   █ █ █   █
## 3|  █ █   █ █ █ █ █
## 2|  █ █ █ █ █ █ █ █
## 1|█ █ █ █ █ █ █ █ █
## 0 ￣￣￣￣￣￣￣￣￣￣￣￣> 
## 
## The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
## Example:
## 
## Input: [1,8,6,2,5,4,8,3,7]
## Output: 49

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        s = 0
        l,r = 0,len(height)-1
        while l < r:
            if height[l] <= height[r]:
                s = max(s,min(height[l],height[r])*(r - l))
                l += 1
            else:
                s= max(s,min(height[l],height[r])*(r - l))
                r -= 1
        return s