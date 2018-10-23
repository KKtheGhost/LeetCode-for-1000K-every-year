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

##这里利用的系统自带的排序功能，有效减少了时间复杂度，从而满足了提交要求。
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        arr = []                                                ##初始化输出列表
        nums.sort()                                             ##对原始列表进行排序，减少后续处理的复杂度
        for i in range(0,len(nums)-2):                          ##对索引i设定边界条件
            if i > 0 and nums[i] == nums[i-1]:                  ##限定i>0是为了i-1越界。当nums[i] == nums[i-1]，跳过本次循环        
                continue                                        ##看上去有点抽象，主要是配合下面的左右紧缩循环。因为nums[i-1]时候走的循环已经遍历完毕了所有解，没有再循环的意义。
            l, r = i+1, len(nums)-1                             ##l=i+1作为第二个值的遍历起点，r=len(nums)-1作为右侧遍历的起点，这样的遍历复杂度最低。
            while l < r:                                        ##限定循环的边界条件
                s = nums[i] + nums[l] + nums[r]                 ##限定遍历的紧缩方式，因为是在有序列表内遍历，所以方便
                if s < 0:                                       ##三个数字总和小于0，说明nums[l]太小了，向右取一个
                    l +=1 
                elif s > 0:                                     ##三个数字总和大于0，说明nums[r]太大了，向左取一个
                    r -= 1
                else:
                    arr.append((nums[i], nums[l], nums[r]))     ##如果三个数总和刚好等于0，说明符合要求
                    while l < r and nums[l] == nums[l+1]:       ##如果nums[l]的下一位和nums[l]相等，那可以多右进一位
                        l += 1
                    while l < r and nums[r] == nums[r-1]:       ##如果nums[r]的下一位和nums[r]相等，那可以多左进一位
                        l += 1
                        r -= 1
                    l += 1; r -= 1                              ##如果没有特殊情况，则在s=0之后，l向右一位，r向左一位
        return arr                                              ##这个遍历方法不会出现重复元素，所以不用去重步骤。
