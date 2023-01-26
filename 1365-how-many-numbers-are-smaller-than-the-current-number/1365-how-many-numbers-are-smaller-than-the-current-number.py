class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp_nums=sorted(nums)
        dct={}
        output=[]*len(nums)
        for indx,num in enumerate(temp_nums):
            if num not in dct:
                dct[num]=indx

        for num in nums:
            output.append(dct[num])
            
        return output
