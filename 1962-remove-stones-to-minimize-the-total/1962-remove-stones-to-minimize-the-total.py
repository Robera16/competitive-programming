class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        for val in piles:
            heapq.heappush(heap, -val)
        
        while k > 0:
            val = -heapq.heappop(heap)
            heapq.heappush(heap, -(val-floor(val/2)))
            k-=1
        
        return -sum(heap)