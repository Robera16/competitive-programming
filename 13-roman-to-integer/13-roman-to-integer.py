class Solution:
    def romanToInt(self, s: str) -> int:
        d=defaultdict(int)
        d['I']=1
        d['V']=5
        d['X']=10
        d['L']=50
        d['C']=100
        d['D']=500
        d['M']=1000
        d['IV']=1
        d['IX']=1
        d['XL']=10
        d['XC']=10
        d['CD']=100
        d['CM']=100
        
        
        rev = s[::-1]
        prev = rev[0:1]
        total=d[prev]
        for char in rev[1:]:
            if d[char+prev]:
                total-=d[char+prev]
            else:
                total+=d[char]
            prev=char
        return total