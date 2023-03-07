class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        accumulator = 0
        prefix = []
        for i in range(len(nums)):
            accumulator += nums[i]
            prefix.append(accumulator)
        return prefix
            