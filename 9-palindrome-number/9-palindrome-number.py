class Solution:
    def isPalindrome(self, x: int) -> bool:
        nums=list(str(x))
        start = 0
        end = len(nums)-1
        while(start < len(nums)):
            if nums[start] != nums[end]:
                break
            start+=1
            end-=1
        return True if (start==len(nums)) else False
        