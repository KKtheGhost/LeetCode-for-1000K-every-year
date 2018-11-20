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

##超时答案，通过不了Submit。复杂度是O(N^2logn)
class Solution:
<<<<<<< HEAD
    def threeSum(self, nums):
=======
    def threeSum(self, nums):                           ##本解法的原理是把3sum问题分解为2sum+1的问题
>>>>>>> 0229a893e36caee8674fa2dba214e502d5a758fe
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
<<<<<<< HEAD
        if len(nums) < 3:
            return []
        result,arr = [],[]
        while 3 <= len(nums):
            j,t = 0,nums[0]
            del nums[0]
            while j < len(nums):
                numt = list(nums)
                s = numt[j]
                del numt[j]
                if -t-s in numt:
                    arr = [t,s,-t-s]
                    arr.sort()
                if arr not in result and arr != []:
                    result.append(arr)
                j += 1
        return result
=======
        if len(nums) < 3:                               ##同样的，如果列表长度不足3则没有意义
            return []
        result,arr = [],[]                              ##初始化输出列表和中转列表
        while 3 <= len(nums):                           ##设定nums的长度边界
            j,t = 0,nums[0]                             ##减少遍历，因此在每次外层循环结束后可以直接在列表中删除走完遍历的元素
            del nums[0]                                 ##因为不进行排序，而列表是有序的，干脆每次用nums[0]，直到列表长度不足
            while j < len(nums):                        ##第二层循环，用了第一层一样的方法，不重复遍历，因此重新生成非共享存储的新列表
                numt = list(nums)                       
                s = numt[j]                             ##对新列表进行操作，获得第一项，删除使用项
                del numt[j]                 
                if -t-s in numt:                        ##对条件进行满足判断
                    arr = [t,s,-t-s]
                    arr.sort()
                if arr not in result and arr != []:     ##如果为真，往输出序列中添加，同时去重处理
                    result.append(arr)
                j += 1
        return result                                   ##最后输出结果
>>>>>>> 0229a893e36caee8674fa2dba214e502d5a758fe
