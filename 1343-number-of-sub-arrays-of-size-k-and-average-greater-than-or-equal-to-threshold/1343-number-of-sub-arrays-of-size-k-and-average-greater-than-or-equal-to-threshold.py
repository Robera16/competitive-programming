class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        target = threshold * k
        summ = 0
        
        for i in range(len(arr)):
            summ+=arr[i]
            if i < k-1:
                continue
            if i > k-1:
                summ-=arr[i-k]
            if summ >= target:
                res+=1
        return res