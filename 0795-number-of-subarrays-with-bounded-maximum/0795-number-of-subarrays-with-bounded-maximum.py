class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
            start=count=cur=0
            
            for i in range(len(nums)):
                
                if left <= nums[i] <= right:
                    cur=i-start+1
                    
                elif nums[i] > right:
                    cur=0
                    start=i+1
                    
                count+=cur
                
            return count