class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        left, right, output = 0,len(nums)-1,0
        
        while left < right:
            if nums[left]+nums[right] < target:
                output+=(right-left)
                left+=1
            else:
                while(right>=0 and nums[left]+nums[right] >= target):
                    right-=1
        return output