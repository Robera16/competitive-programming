class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n > 1:
            return self.isPowerOfFour(n/4)
        elif n==1:
            return True
        else:
            return False