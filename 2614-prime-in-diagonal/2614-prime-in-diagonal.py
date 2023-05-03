class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        n=len(nums)
        prime, output= False, 0
        
        def is_prime(x: int)->bool:
            d=2
            while d*d<=x:
                if x%d==0:
                    return False
                d+=1
            return True
        
        
        for i in range(n):
            if is_prime(nums[i][i]):
                output=max(output, nums[i][i])
                prime=True
            if is_prime(nums[i][n-1-i]):  
                output=max(output, nums[i][n-1-i])
                prime=True
        
        if prime and output!=1:
            return output
        return 0
        
        