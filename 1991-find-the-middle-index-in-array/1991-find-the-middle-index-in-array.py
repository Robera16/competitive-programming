class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total=0
        prefix_sum=[]
        for val in nums:
            total+=val
            prefix_sum.append(total)
        
        left_sum=[0]+prefix_sum
        for i in range(len(nums)):
            if left_sum[i]==total-prefix_sum[i]:
                return i
        return -1