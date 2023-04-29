class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD=10**9+7
        even_count, odd_count = 5, 4
  
        if n%2==0:
            mult=n//2
            return (pow(even_count,mult,MOD)*pow(odd_count,mult, MOD))%MOD
        else:
            mult=n//2
            return (pow(even_count,mult+1,MOD)*pow(odd_count,mult,MOD))%MOD
            
#         for i in range(n):
#             if i%2==0:
#                 output*=even_count
#             else:
#                 output*=odd_count
                
            
#         return output%MOD
        
        
#         def goodNum(count):
#             if count==n:
#                 if count%2!=0:
#                     return even_count
    
#                 return odd_count
            
#             if count%2!=0:
#                 return even_count*(goodNum(count+1))
#             else:
#                 return odd_count*(goodNum(count+1))
                
        
#         answer = goodNum(1)
        
#         print(answer)
#         return answer%MOD