class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        output=[]
        while len(nums):
            output.append(nums.pop(0)+nums.pop())
        return max(output)