class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq._heapify_max(stones)
        while len(stones) > 1:
            y=heapq._heappop_max(stones)
            x=heapq._heappop_max(stones)
            if x!=y:
                heapq.heappush(stones, y-x)
                heapq._heapify_max(stones)
            if len(stones)==0:
                return y-x
        return  heapq._heappop_max(stones)