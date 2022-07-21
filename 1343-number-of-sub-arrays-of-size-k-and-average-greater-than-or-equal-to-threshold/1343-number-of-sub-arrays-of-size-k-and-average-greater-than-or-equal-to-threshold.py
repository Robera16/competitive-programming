class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        summ=sum(arr[:k])
        output=0
        if summ/k >= threshold:
            output+=1
        i=k
        while(i < len(arr)):
            summ=summ+arr[i]-arr[i-k]
            if summ/k >= threshold:
                output+=1
            i+=1
        return output
             