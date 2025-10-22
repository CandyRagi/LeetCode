# Version 1

class Solution(object):
    def removeDuplicates(self, nums):
        uniqueNums=[] 
        for num in nums:
            found=False
            for uniqueNum in uniqueNums:
                if(num==uniqueNum):
                    found=True
                    break

            if(found==False):
                uniqueNums.append(num)

        nums=uniqueNums       
    
        return len(uniqueNums)
    
# Version 2

class Solution(object):
    def removeDuplicates(self,nums):
        i=1
        while(i<len(nums)):
            flag=False
            for j in range(i-1):
                if(nums[j]==nums[i]):
                    nums.pop(i)
                    flag=True
                    break
            
            if(flag==False):
                i+=1

        return i        




