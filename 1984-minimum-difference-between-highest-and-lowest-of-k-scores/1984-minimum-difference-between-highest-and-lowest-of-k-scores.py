class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        output=100001
        for i in range(len(nums)):
            output=min(output, nums[i+k-1]-nums[i])
            if i+k==len(nums):    
                return output
            