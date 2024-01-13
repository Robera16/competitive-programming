class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]+1
        
        # find the longest prefix sum
        summ=0
        for i in range(len(nums)):
            summ+=nums[i]
            if i<len(nums)-1 and nums[i+1]!=nums[i]+1:
                break
        # finding missing x in nums,  x>=summ       
        while summ in nums:
            summ+=1
        
        return summ