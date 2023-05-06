class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        k = 0 
        output = 0
        
        for i in range(n):
            k|=nums[i]
        
        subsets = []
        for i in range(len(nums) + 1):
            subsets.extend(list(combinations(nums, i)))

        for subset in subsets:
            if k == self.bitwiseOR(list(subset)):
                output+=1
            
                
        return output
        
    def bitwiseOR(self, temp):
        res = 0
        for num in temp:
            res|=num
        return res