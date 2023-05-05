class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        for i in range(n+1): # i-> 0,1,2,3
            result ^= i  # 0^0^1^2^3 result = 2
        
        for val in nums:
            result ^= val # (0^0^1^2^3) ^ (3^0^1)
        
        # applying commutative property
        # (0^0^1^2^3) ^ (3^0^1)
        # (0^0^0)^(1^1)^(2)^(3^3)
        # 0^0^2^0 
        # 2
        return result
        
        # Gaussian formula
        # n = len(nums)
        # return (n*(n+1))//2 - sum(nums)