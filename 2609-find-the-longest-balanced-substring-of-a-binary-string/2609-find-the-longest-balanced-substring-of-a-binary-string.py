class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        output, zero_count, one_count, prev = 0, 0, 0, 2
        for val in s:
            if val=='0':
                if prev=='1':
                    output = max(output, (min(zero_count, one_count)*2))
                    zero_count, one_count = 0, 0
                zero_count+=1
            else:
                one_count+=1
            prev=val
        output = max(output, (min(zero_count, one_count)*2))
        return output