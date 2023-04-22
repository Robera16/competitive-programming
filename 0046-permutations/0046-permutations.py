class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output=[]
        def permutation(curr):
            if len(curr)==len(nums):
                output.append(curr.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] in curr: continue
                curr.append(nums[i])
                permutation(curr)
                curr.pop()   
            
        permutation([])
        return output