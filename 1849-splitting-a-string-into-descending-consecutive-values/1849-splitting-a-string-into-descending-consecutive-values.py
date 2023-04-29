class Solution:
    def splitString(self, s: str) -> bool:
        
        def dfs(index, prev):
            if index==len(s):
                return True
            
            for j in range(index, len(s)):
                val=int(s[index: j+1])
                if val+1==prev and dfs(j+1, val): 
                    return True
            
            return False
        
        
        n=len(s)
        for i in range(n-1):
            first_val=int(s[:i+1])
            if dfs(i+1, first_val):
                return True
            
        return False