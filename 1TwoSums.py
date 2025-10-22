
# My solution
class Solution(object):
    def twoSum(self,nums,target):
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if(nums[i]+nums[i+j+1]==target):
                    return [i,i+j+1]

        return [-1,-1]

# AI Solution
class Solution(object):
    def twoSum(self, nums, target):
        seen = {}  # {number: index}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:  # Found pair!
                return [seen[complement], i]
            seen[num] = i  # Store current
        return [-1, -1]