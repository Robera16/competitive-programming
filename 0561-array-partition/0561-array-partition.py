class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        output, p = 0, 0
        nums.sort()
        while p < len(nums):
            output+=nums[p]
            p+=2
            
        return output