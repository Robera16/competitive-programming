class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        
        if len(nums)==0 or val not in nums:
            return len(nums)
        
        index=nums.index(val)
        while(nums[index]==val):
            if index==len(nums)-1:
                nums.pop()
                return len(nums)
            else:
                del nums[index]
        
        return len(nums)
        