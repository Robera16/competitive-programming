class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxAvg = -inf
        windowAvg = 0
        start = 0
        windowSum = 0
    
        for i in range(len(nums)):
            windowSum += nums[i]
        
            if ((i - start + 1) == k):
                windowAvg = windowSum/k
                maxAvg = max(maxAvg, windowAvg)
                windowSum -= nums[start]
                start += 1
    
        return maxAvg