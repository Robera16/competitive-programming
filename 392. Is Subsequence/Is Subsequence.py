class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1=0
        if len(s)==0:
            return True
        for char in t:
            if s[p1] == char:
                p1+=1      
            if p1 == len(s):
                return True
        return False