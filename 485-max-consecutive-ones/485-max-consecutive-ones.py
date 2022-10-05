class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        output,count=0,0
        for val in nums:
            if val==1:
                count+=1
            else:
                output=max(output, count)
                count=0
            
        return max(output, count)