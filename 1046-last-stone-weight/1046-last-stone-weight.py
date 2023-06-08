class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:


        for i in range(len(stones)):
            stones[i]=-stones[i]
        
        # print(stones)
        heapq.heapify(stones)
        # print(stones)
        while len(stones)>=2:
            s1 = -(heapq.heappop(stones))
            s2 = -(heapq.heappop(stones))
            
            if s1!=s2:
                heapq.heappush(stones, -(s1-s2))
        
        if len(stones):
            return -(stones[-1])
        else:
            return 0


        # heapq._heapify_max(stones)
        # while len(stones) > 1:
        #     y=heapq._heappop_max(stones)
        #     x=heapq._heappop_max(stones)
        #     if x!=y:
        #         heapq.heappush(stones, y-x)
        #         heapq._heapify_max(stones)
        #     if len(stones)==0:
        #         return y-x
        # return  heapq._heappop_max(stones)