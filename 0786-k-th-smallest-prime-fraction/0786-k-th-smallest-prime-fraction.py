class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                heapq.heappush(heap, (arr[i]/arr[j], [arr[i], arr[j]]))
  
        while k > 1:
            heapq.heappop(heap)
            k-=1
        return heapq.heappop(heap)[1]