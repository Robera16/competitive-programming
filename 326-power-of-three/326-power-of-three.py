class Solution:
    def isPowerOfThree(self, n: int) -> bool:    
        if n > 1:
            return self.isPowerOfThree(n/3)
        elif n==1:
            return True
        elif n==0:
            return False 
        
        
        
