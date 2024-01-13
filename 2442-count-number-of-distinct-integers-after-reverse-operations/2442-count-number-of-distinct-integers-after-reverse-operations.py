class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            num=str(nums[i])
            nums.append(int(num[::-1]))
        
        return len(set(nums))