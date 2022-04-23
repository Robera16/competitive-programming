class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output=[0]*len(nums)
        i=0
        j=1
        while(i < len(nums)-1):
            if j==len(nums):
                i+=1
                j=i+1
            elif nums[i] > nums[j]:
                output[i]+=1
                j+=1
            else:
                if nums[i]!=nums[j]:
                    output[j]+=1
                j+=1
            
        return output