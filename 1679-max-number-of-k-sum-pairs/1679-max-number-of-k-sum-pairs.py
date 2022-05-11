class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort() 
        operations=0      
        while(len(nums)>=2):
            if nums[0]+nums[-1]==k:
                nums.pop(0)
                nums.pop()
                operations+=1
            elif nums[0]+nums[-1]>k:
                nums.pop()
            else:
                nums.pop(0)
        return operations
        