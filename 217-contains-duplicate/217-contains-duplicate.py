class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for g in range(len(nums)):
            if g==len(nums)-1:
                return False
            elif nums[g] == nums[g+1]:
                return True
        
            