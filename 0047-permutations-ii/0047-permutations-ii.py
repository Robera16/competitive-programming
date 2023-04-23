class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        output=[]
        def permute(comb, counter):
            if len(comb)==len(nums):
                output.append(list(comb))
                return
            
            for num in counter:
                if counter[num]>0:
                    comb.append(num)
                    counter[num]-=1
                    permute(comb, counter)
                    comb.pop()
                    counter[num]+=1
                    
        permute([], Counter(nums))
        return output
        
        
#         output=[]
#         self.dfs(nums, [], output)
#         return output
    
#     def dfs(self, nums, path, output):  
#         if not nums and path not in output:
#             output.append(path)
        
#         for i in range(len(nums)):
#             self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], output)
        