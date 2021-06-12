class Solution:
    def twoSum(self, nums, target):
        
      required = {}
      for i in range(len(nums)):
        v = target - nums[i]
        if v in required: 
            return [required[target - nums[i]],i]
        else:
            required[nums[i]]=i