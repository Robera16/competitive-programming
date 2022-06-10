class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        t=sum(nums)
        l=0
        for i in range(len(nums)):
            r=t-nums[i]-l
            if r==l:
                return i
            l+=nums[i]
        return -1
        