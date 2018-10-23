class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = len(height)
        a,p1,p2 = 0,0,l-1
        while p1<p2:
            a = max(a,min(height[p1],height[p2])*(p2-p1))
            if height[p1]<height[p2]:
                p1+=1
            else:
                p2-=1
        return a