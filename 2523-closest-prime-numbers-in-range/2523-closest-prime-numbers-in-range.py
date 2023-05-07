class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        output, answer, minn, nums1 = [], [-1, -1], float('inf'), float('inf')
        prime_numbers = self.sieve_prime(right)
        
    
        for i in range(left, right+1):
            if prime_numbers[i]:
                output.append(i)
        
        for i in range(len(output)-1):
            diff = output[i+1] - output[i]
            if  (diff < minn) or (diff==minn and (output[i] < nums1)):
                answer[0], answer[1] = output[i], output[i+1]
                minn = diff
                nums1 = output[i]
        
        return answer
        
        
    def sieve_prime(self, x: int) -> list:
        is_prime = [True for _ in range(x+1)]
        is_prime[0]=is_prime[1]=False

        i=2
        while i*i<=x: 
            if is_prime[i]:
                j = i*i 
                while j<=x:
                    is_prime[j]=False
                    j+=i
            i+=1

        return is_prime
        
        
        
#         output, answer, minn, nums1 = [], [-1, -1], float('inf'), float('inf')
#         for num in range(left, right+1):
#             if self.is_prime(num):
#                 output.append(num)
        
        
#         for i in range(len(output)-1):
#             diff = output[i+1] - output[i]
#             if  (diff < minn) or (diff==minn and (output[i] < nums1)):
#                 answer[0], answer[1] = output[i], output[i+1]
#                 minn = diff
#                 nums1 = output[i]
        
#         return answer
    
#     def is_prime(self, x: int) -> bool:
#         if x <=1:
#             return False
#         d=2
#         while d*d<=x:
#             if x%d==0:
#                 return False
#             d+=1
#         return True