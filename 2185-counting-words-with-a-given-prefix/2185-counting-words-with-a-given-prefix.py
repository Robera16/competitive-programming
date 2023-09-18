class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        length = len(pref) 
        output = 0
        for word in words:
            if word[:length] == pref:
                output+=1
                
        return output
            