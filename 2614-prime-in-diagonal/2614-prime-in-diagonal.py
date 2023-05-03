class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        
        n, output= len(nums), 0
    
        for i in range(n):
            if self.is_prime(nums[i][i]):
                output=max(output, nums[i][i])
                
            if self.is_prime(nums[i][n-1-i]):  
                output=max(output, nums[i][n-1-i])
                
        if output and output!=1:
            return output
        return 0
        
    def is_prime(self, x: int)->bool:
        d=2
        while d*d<=x:
            if x%d==0:
                return False
            d+=1
        return True