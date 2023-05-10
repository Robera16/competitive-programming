class Solution:
    def countArrangement(self, n: int) -> int:
        
        nums = []
        beautiful_arrangements = 0
        
        for i in range(1, n+1):
            nums.append(i)
                    
        
        
        def permutation(curr):
            nonlocal beautiful_arrangements
            if len(curr)==len(nums):
                beautiful_arrangements += 1
                return
            
            for i in range(len(nums)):
                if nums[i] in curr: continue
                
                if (len(curr)+1)%nums[i]!=0 and nums[i]%(len(curr)+1)!=0: 
                    continue
                
                curr.append(nums[i])
                permutation(curr)
                curr.pop()   
            
        permutation([])
        
        return beautiful_arrangements
    
    
    
    
    
    
#     def dfs(self, nums, path, output):
#         if not nums:
#             flag = True
#             for i, val in enumerate(path):
#                 if (i+1)%val!=0 and val%(i+1)!=0:
#                     flag = False
#                     break
                    
#             if flag:
#                 output.append(path)
            
#         for i in range(len(nums)):
#             self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], output)