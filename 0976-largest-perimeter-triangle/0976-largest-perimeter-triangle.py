class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        """
            A triangle is valid if sum of any of its two sides is greater than the third side
            (a + b <= c) or (a + c <= b) or (b + c <= a) return false
        """
        nums.sort()
        for i in range(len(nums)-1, 1, -1):
            if nums[i-2] + nums[i-1] > nums[i]:
                return nums[i-2] + nums[i-1] + nums[i]
        return 0