class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for v in nums:
            if nums.count(v)==1:
                return v