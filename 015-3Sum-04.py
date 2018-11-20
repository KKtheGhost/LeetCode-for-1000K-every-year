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

##最强的方法，只要300ms不到，膜拜。
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        count = {}
        for n in nums:
            if n not in count:
                count[n] = 0
            count[n] += 1
        
        pos, neg = [], []
        for n in count:
            if n > 0:
                pos.append(n)
            elif n < 0:
                neg.append(n)
        
        res = []
        if 0 in count:
            if count[0] > 2:
                res.append([0, 0, 0])
        if len(pos) == 0 or len(neg)==0:
            return res
        pos.sort()
        neg.sort()
        for i in pos:
            for j in neg:
                t = 0 - i -j
                if t in count:
                    if t==i and t==j and count[t]>2:
                        res.append([i,j,t])
                    elif (t == i) or (t == j):
                        if count[t] > 1:
                            res.append([i, j, t])
                    elif (t > i) or (t < j) or (t==0):
                        res.append([i, j, t])
        return res
