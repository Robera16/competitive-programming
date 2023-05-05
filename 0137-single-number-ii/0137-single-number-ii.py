class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return int(round((sum(set(nums)) - sum(nums)/3)*1.5))
        