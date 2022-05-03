class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        startingIndex=0
        endingIndex=len(nums)-1
        numsCopy=list(nums)
        n=len(nums)
        while(min(nums)==nums[0]):
            nums.pop(0)
            if not len(nums):
                break
            startingIndex+=1
            
        
        while(max(numsCopy)==numsCopy[-1]):
            numsCopy.pop()
            if not len(numsCopy):
                break
            endingIndex-=1
            
        
        if (startingIndex==endingIndex) or (startingIndex==n-1 and endingIndex==0):
            return 0
        else:
            return (endingIndex-startingIndex)+1