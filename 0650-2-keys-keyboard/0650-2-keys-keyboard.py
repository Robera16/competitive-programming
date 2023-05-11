class Solution:
    def minSteps(self, n: int) -> int:
        # a aa aaaa aa aa aa
        # c  pc p    p  p  p
        # cpcppp
        ans = 0
        d = 2
        while n > 1:
            while n % d == 0:
                ans += d
                n /= d
            d += 1
        return ans
        