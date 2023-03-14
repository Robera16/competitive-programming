class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n==0:
            return 1
        elif n < 0:
            return 1/self.reve(x, abs(n))
        else:
            return self.reve(x, abs(n))
        
    
    def reve(self, x, n):
        if n==0:
            return 1
        if n % 2 == 0:
            return self.reve(x*x, n//2)
        else:
            return x*self.reve(x*x, (n-1)//2)