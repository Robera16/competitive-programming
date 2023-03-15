class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        AABABBA
        
        1, unique
        2, for each unique sliding
        3  max_wind_size
        """
        uniques = set(s)
        max_size = 0
        temp = k
        for char in uniques:
            l,r,k=0, 0, temp
            while r < len(s):
                if s[r]!=char:
                    k-=1
                    
                while k < 0 and l<=r:
                    if s[l]!=char:
                        k+=1
                    l += 1
                    
                if k>=0:
                    max_size = max(max_size, (r-l+1))
                    
                r+=1
                
        return max_size
        