class Solution(object):
    def twoSum(self, nums, target):
        keys = {}
        for i in range(len(nums)):
            if target - nums[i] in keys:
                return [keys[target - nums[i]], i]
            if nums[i] not in keys:
                keys[nums[i]] = i      
