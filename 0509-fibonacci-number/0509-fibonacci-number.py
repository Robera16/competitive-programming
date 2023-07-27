class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        def fib(n):
            if n==0:
                return 0
            if n==1 or n==2:
                return 1
            
            if n in memo:
                return memo[n]
            
            result = self.fib(n-1)+self.fib(n-2)
            memo[n] = result

            return result
        
        return fib(n)