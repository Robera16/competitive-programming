class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        
        if len(nums)==0 or val not in nums:
            return len(nums)
        
        index=nums.index(val)
        # print(index)
        while(nums[index]==val):
            if index==len(nums)-1:
                nums.pop()
                return len(nums)
            else:
                # nums.pop(index)
                del nums[index]
        
        return len(nums)
        