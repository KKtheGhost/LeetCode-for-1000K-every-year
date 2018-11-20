class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        ## 不满足空间度O(log(m+n)),但是最高效
        l=sorted(nums1+nums2)
        a=len(l)
        if a%2==0:
            return (l[a/2-1]+l[a/2])/2.0
        else:
            return l[a/2]