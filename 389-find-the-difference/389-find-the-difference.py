class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sLetters=list(s)
        tLetters=list(t)
        
        for letter in sLetters:
            tLetters.remove(letter)
        
        return tLetters[0]
        
        
        