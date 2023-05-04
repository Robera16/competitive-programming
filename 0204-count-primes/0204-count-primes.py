class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=1:
            return 0
        
        return self.sievePrime(n)
    
    # Sieve of Erathosthenes approach
    def sievePrime(self, x: int) -> int:
        is_prime = [True for i in range(x)]
        is_prime[0]=is_prime[1]=False
        
        i = 2
        while i*i<=x:
            if is_prime[i]:
                j = i*i
                while j<x:
                    is_prime[j]=False
                    j+=i
            i+=1
        return is_prime.count(True)