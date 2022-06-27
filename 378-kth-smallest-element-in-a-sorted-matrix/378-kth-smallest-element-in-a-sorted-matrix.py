class Solution(object):
    def kthSmallest(self, matrix, k):
        stack=[]
        for val in matrix:
            for i in val:
                heapq.heappush(stack, i)
    
        while(k-1):
            heapq.heappop(stack)
            k-=1
        return heapq.heappop(stack)