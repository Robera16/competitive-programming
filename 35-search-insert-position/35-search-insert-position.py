class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        val=0
        try:
            val = nums.index(target)    
        except:
            nums.append(target)
            nums.sort()
            val = nums.index(target)
        return val