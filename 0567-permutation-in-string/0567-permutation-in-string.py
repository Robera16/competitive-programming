class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
           dcts1={
             a:1
             b:1
            }
            
            dcts2={
                b:1
                a:1
            }
            
            s1='ab'
            s2="eidbaooo"
            
        """
        dcts1={}
        for char in s1:
            if char in dcts1:
                dcts1[char] += 1
            else:
                dcts1[char] = 1
        
        
        left, right = 0, 0
        dcts2={}
        while right < len(s2):
            char = s2[right]
            if char in dcts2:
                dcts2[char] += 1
            else:
                dcts2[char] = 1
                
            if (right - left)+1 == len(s1):
                if dcts1==dcts2:
                    return True
                else:
                    if dcts2[s2[left]]==1:
                        dcts2.pop(s2[left])
                    else:
                        dcts2[s2[left]]-=1
                        
                    left+=1
                    
            right+=1      
        return False