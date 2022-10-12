class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        N = len(nums)
        q = collections.deque()
        res = math.inf
        # prefix sum list--------------------------------------
        psum = [0] * (N + 1)
        for i in range(1, N + 1):
            psum[i] = psum[i - 1] + nums[i - 1]
        # If a value in prefix sum list comes which is less than the previous one in it, we will keep on poping indexes from the queue until its position comes, keeping the queue monotonically increasing.
        for ptr , temp in enumerate(psum):
            # release and collect answers----------------------
            while q and temp <= psum[q[-1]]:
                q.pop()
            
            while q and temp - psum[q[0]] >= k:
                res = min(res, ptr - q.popleft())
            
            # acquire------------------------------------------
            q.append(ptr)
        
        return res if res != math.inf else -1