class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0]
        for i in range(1, n+1):
            output.append(output[i>>1]+i%2)
        return output
        
        # (n)
#         output = [0, 1]
#         for i in range(2, n+1):
#             res = i//2
#             if i%2==0:
#                 output.append(output[res])
#             else:
#                 output.append(output[res]+1)
                
#         return output[:n+1]
        
        
         # O(nlogn)
#         output = []
        
#         for i in range(n+1):
#             output.append(bin(i).count('1')) 
        
#         return output