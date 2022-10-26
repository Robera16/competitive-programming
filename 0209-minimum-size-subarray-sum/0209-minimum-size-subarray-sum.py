class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        subarray_sum=0
        size=len(nums)
        start,end=0,0
        
        for i in range(len(nums)):
            subarray_sum+=nums[i]
            if subarray_sum >= target:
                size=min(size, i+1-start)
                while(subarray_sum > target):
                    subarray_sum-=nums[start]
                    start+=1
                    if subarray_sum>=target:
                        size=min(size, i+1-start)
        if size==len(nums) and start==0 and subarray_sum<target:
            return 0
        return size
                
        