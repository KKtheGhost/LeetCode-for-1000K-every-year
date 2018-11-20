## Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
## 
## Example:
## 
## Given array nums = [-1, 2, 1, -4], and target = 1.
## 
## The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

##问题本身其实就是一个求3sum和target的最小差的问题，很类似于3Sum，也是先对列表排序
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """ 
        nums.sort()                                             ##对列表排序
        mindiff = target - sum(nums[:3])                        ##因为是有序数组，循环从左开始遍历，所以初始最小差就是target - sum(nums[:3]
        for i in range(len(nums)-2):                            ##限定i的边界
            l,r = i+1,len(nums)-1                               ##限定l和r边界
            while l < r:                                        ##限定内循环的边界，l<r
                diff = target - nums[i] - nums[l] - nums[r]     ##获得每次循环后的差diff
                if abs(diff) <= abs(mindiff):                   ##如果绝对值diff比绝对值mindiff要小
                    mindiff = diff                              ##说明这组组合更加接近target，更新mindiff
                if diff > 0:                                    ##如果diff大于0.说明target比和要大，所以要让和更大，l右移一位
                    l += 1
                elif diff < 0:                                  ##如果diff小于0.说明target比和要小，所以要让和更小，r左移一位
                    r -= 1
                else:
                    return target                               ##如果diff == 0了，那就直接输出target得了，还等什么。
        return target - mindiff                                 ##最后target减去mindiff就是答案