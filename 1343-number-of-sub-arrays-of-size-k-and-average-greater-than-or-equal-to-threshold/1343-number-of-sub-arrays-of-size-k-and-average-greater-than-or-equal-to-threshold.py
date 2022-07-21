class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        summ=0
        output=0
        for i in range(k):
            summ+=arr[i]
        if summ/k >= threshold:
            output+=1
        i+=1
        while(i < len(arr)):
            summ=summ+arr[i]-arr[i-k]
            if summ/k >= threshold:
                output+=1
            i+=1
        return output
             