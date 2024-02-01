class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        seeker, placeholder = 0, 1
        while placeholder < len(nums):
            if nums[placeholder]!=0:
                while seeker < placeholder:
                    if nums[seeker]==0:
                        nums[seeker]=nums[placeholder]
                        nums[placeholder]=0
                        seeker+=1
                        break
                    else:
                        seeker+=1
            placeholder+=1
            
        return nums
        