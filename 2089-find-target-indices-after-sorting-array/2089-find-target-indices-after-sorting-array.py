class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        list=[]
        nums.sort()
        
        if target in nums:
            i=nums.index(target)
            list.append(i)
            i+=1
            while(i<len(nums) and nums[i]==target):
                list.append(i)
                i+=1
        return list