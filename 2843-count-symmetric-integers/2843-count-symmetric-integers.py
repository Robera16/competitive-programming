class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        output=0
        for num in range(low, high+1):
            num=str(num)
            n=len(num)
            if n%2==0:
                left=num[:n//2]
                right=num[n//2:]
                
                if sum(map(int, left))==sum(map(int, right)):
                    output+=1
                    
        return output