class Solution:
    def minSwaps(self, s: str) -> int:
        count=0
        for char in s:
            if count and char != '[':
                count -= 1
            else:
                count += 1
                
        return (count + 1) //2
#         opening, closing = 0, len(s)-1
#         openingCount, closingCount = 0, 0
#         char_list = [char for char in s]
#         output = 0
#         # print(openingPointer, closingPointer)
#         # print(openingCount, closingCount)
#         # print(char_list)
        
#         while opening < closing:
#             if s[opening] == '[':
                
#                 openingCount += 1
#             else: # s[opening] == ']'
#                 closingCount += 1 
                
#                 if closingCount > openingCount:
#                     while s[closing] != '[':
#                         closing -= 1
                        
#                     char_list[opening], char_list[closing] = char_list[closing], char_list[opening]
#                     closingCount -= 1
#                     output += 1
#                     print(char_list)
#             opening += 1
        
       
#         return output-1