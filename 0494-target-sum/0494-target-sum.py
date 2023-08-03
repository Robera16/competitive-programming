class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memory = {}
        
        def dp(i, total):
            if i == len(nums):
                return int(total == target)
            if (i,total) in memory:
                return memory[(i, total)]
            memory[(i, total)] = (dp(i+1, total + nums[i]) + dp(i+1, total-nums[i]))
            return memory[(i, total)]

        return dp(0,0)