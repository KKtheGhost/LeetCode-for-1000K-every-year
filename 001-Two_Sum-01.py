##Given an array of integers, return indices of the two numbers such that they add up to a specific target.
##
##You may assume that each input would have exactly one solution, and you may not use the same element twice.
##
##Example:
##
##Given nums = [2, 7, 11, 15], target = 9,
##
##Because nums[0] + nums[1] = 2 + 7 = 9,
##return [0, 1].

##需要返回的值只是两个索引组成的列表！！
class Solution(object):
    def twoSum(self, nums, target):
        keys = {}                                       ##创建一个空字典
        for i in range(len(nums)):                      ##进行循环遍历，保证i不大于列表nums的元素个数
            if target - nums[i] in keys:                ##条件判断，如果(target - nums[i])的值也在字典里，则返回结果
                return [keys[target - nums[i]], i]
            if nums[i] not in keys:                     ##条件判断，如果字典中没有nums[i]，则把nums[i]的键设为i，从而保证遍历
                keys[nums[i]] = i      
