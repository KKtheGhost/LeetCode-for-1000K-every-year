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

##超时答案，通过不了Submit。复杂度是O(N^3)
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
<<<<<<< HEAD
        if len(nums) < 3:
            return []
        a,i = [],0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                k = j + 1
                while k < len(nums):
                    if nums[i] + nums[j] + nums[k] == 0:
                        b = [nums[i],nums[j],nums[k]]
                        b.sort()
                        if b not in a:
=======
        if len(nums) < 3:                                   ##如果字符串nums的长度小于3，则没有意义，所以输出[]
            return []       
        a,i = [],0                                          ##初始化输出字符串和索引i    
        while i < len(nums):                                ##第一层循环，遍历所有含有nums[i]的情况
            j = i + 1                                       ##每次循环结束初始化第二层循环的索引j
            while j < len(nums):                            ##第二层循环，遍历nums[i]的情况下，所有含有nums[j]的情况
                k = j + 1                                   ##每次循环结束初始化第三层循环的索引k
                while k < len(nums):                        ##第三层循环，n^3层的循环
                    if nums[i] + nums[j] + nums[k] == 0:    ##设定真假判断条件
                        b = [nums[i],nums[j],nums[k]]       ##获得符合条件的字符列表
                        b.sort()
                        if b not in a:                      ##排序后去重
>>>>>>> 0229a893e36caee8674fa2dba214e502d5a758fe
                            a.append(b)
                    k += 1
                j += 1
            i += 1
<<<<<<< HEAD
        return a
=======
        return a                                            ##最后输出结果
>>>>>>> 0229a893e36caee8674fa2dba214e502d5a758fe
