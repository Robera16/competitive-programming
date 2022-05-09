class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        output=[]
        sPointer=0
        ePointer=len(nums)-1
        
        while(sPointer < ePointer):
            output.append(nums[sPointer])
            sPointer+=1
            output.append(nums[ePointer])
            ePointer-=1
            if sPointer==ePointer:
                output.append(nums[sPointer])
        return output