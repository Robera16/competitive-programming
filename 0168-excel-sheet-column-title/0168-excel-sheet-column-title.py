class Solution:
    def convertToTitle(self, columnNumber: int) -> str:       
        ans=""        
        while columnNumber>0:
            c=chr(ord('A')+(columnNumber-1)%26)
            ans=c+ans
            columnNumber=(columnNumber-1)//26            
        return ans   