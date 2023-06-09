class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        heap = [(nums[0], 1)]
        for num in nums[1:]:
            val, l = heapq.heappop(heap)
            while val + 1 < num:
                if l < 3:
                    return False
                    
                if len(heap) == 0:
                    break
                    
                val, l = heapq.heappop(heap)
            
            if num == val + 1:
                heapq.heappush(heap, (num, l + 1))
            elif num == val:
                heapq.heappush(heap, (val, l))
                heapq.heappush(heap, (num, 1))
            else:  # heap is empty
                heapq.heappush(heap, (num, 1))
                
        while len(heap):
            val, l = heapq.heappop(heap)
            if l < 3:
                return False
            
        return True