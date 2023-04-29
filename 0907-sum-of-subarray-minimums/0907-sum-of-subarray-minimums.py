class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
       
        MOD, stack , sum_of_minimums = 10**9+7, [], 0
        
        for i in range(len(arr)+1):

            while stack and (i==len(arr)  or arr[stack[-1]]>=arr[i]):
                mid = stack.pop()
                next_smaller = i
                previous_smaller = stack[-1] if stack else -1
                count = (mid-previous_smaller)*(next_smaller-mid)
                
                sum_of_minimums+=(arr[mid]*count)
            
            stack.append(i)
        
        return sum_of_minimums%MOD

        