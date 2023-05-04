def almost_prime(x: int) -> set:
    d=2
    factorization = set()
    
    while d*d<=x:
        while x%d==0:
            factorization.add(d)
            x//=d
        d+=1
    
    if x > 1:
        factorization.add(x)
    
    return factorization
    
n = int(input())
output = 0

for i in range(1, n+1):
    
    prime_factors = almost_prime(i)
    if len(prime_factors)==2:
        output+=1

print(output)