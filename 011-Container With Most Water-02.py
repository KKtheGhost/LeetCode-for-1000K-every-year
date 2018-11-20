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

##基本就是一个多项求最值的遍历问题，范围已经被数组长度和数值框定了，比较简单
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        s = 0
        l,r = 0,len(height)-1                                   ##设定两个边界值l和r，代表最左边的数值坐标和最右边的数值坐标
        while l < r:                                            ##只有l<r时面积才有意义，限定循环范围
            if height[l] <= height[r]:                          ##当左边的数值比右边短时
                s = max(s,min(height[l],height[r])*(r - l))     ##在‘缓存中的最大值s’、‘当前框内面积’里面取最大值，赋值给s
                l += 1                                          ##因为height[l]较小，所以l+1继续遍历寻找
            else:                                               ##方法同上，因为height[r]较小，所以r-1继续遍历寻找
                s= max(s,min(height[l],height[r])*(r - l))
                r -= 1
        return s                                                ##最后输出遍历后的最大值s