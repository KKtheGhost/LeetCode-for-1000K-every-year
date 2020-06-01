class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(nums)):
            if (target - nums[i]) in dic:
                return [i,dic[target-nums[i]]]
            dic[nums[i]] = i 
