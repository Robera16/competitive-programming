class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start,counter=0,0
        for i in range(1,len(nums)):
            if nums[start]==nums[i] and counter==0:
                start+=1
                nums[start]=nums[i]
                counter=1
            if nums[start]!=nums[i]:
                start+=1
                nums[start]=nums[i]
                counter=0
        return start+1