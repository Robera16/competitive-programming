class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest, largest = min(nums), max(nums)
        return self.GCD(largest, smallest)
    
    def GCD(self, a, b):
        if b==0:
            return a
        
        return self.GCD(b, a%b)