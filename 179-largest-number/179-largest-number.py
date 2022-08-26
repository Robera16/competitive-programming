class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for index, element in enumerate(nums):
            nums[index]=str(element)
        
        def compare(n1,n2):
            return -1 if n1 + n2 > n2 + n1 else 1
        nums = sorted(nums, key=cmp_to_key(compare))
        return str(int("".join(nums)))