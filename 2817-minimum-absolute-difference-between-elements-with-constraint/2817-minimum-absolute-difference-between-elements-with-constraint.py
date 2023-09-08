from sortedcontainers import SortedList

class Solution:
    def minAbsoluteDifference(self, nums, x):
        ans = float('inf')
        bst = SortedList([-float('inf'), float('inf')])
        size = len(nums)
        for i in range(x, size):
            bst.add(nums[i])
        left = x
        
        for i, v in enumerate(nums):
            t = bst.bisect_left(v)
            ans = min(ans, bst[t] - v, v - bst[t-1])
            bst.remove(nums[left])
            left += 1
            if left == size:
                break
        
        return ans