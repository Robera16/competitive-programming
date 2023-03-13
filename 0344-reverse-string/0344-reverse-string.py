class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        i, j= 0, len(s)-1
        self.reve(s, i, j)
    
    def reve(self, s, i, j):
        if i>=j:
            return
        else:
            s[i],s[j] = s[j], s[i]
            i+=1
            j-=1
            self.reve(s, i, j)

        
