class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        
        nums = [0,1]
        i=2
        while i < n+1:
            if i % 2 == 0:
                nums.append(nums[i // 2])
                
            else:
                nums.append(nums[i // 2] + nums[(i//2) + 1])
            i+=1
        return max(nums)

                
            
            
        