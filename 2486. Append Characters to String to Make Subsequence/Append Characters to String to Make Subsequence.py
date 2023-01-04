class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        pt=0
        for char in s:
            if pt < len(t) and char == t[pt]:
                pt+=1
        return len(t)-pt