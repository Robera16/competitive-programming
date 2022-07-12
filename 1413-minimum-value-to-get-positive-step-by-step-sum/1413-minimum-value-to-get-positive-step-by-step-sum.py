class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        output=1
        summ=0
        for val in nums:
            summ+=val
            if summ<0 and abs(summ) >= output:
                output=abs(summ)+1
        return output