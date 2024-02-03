class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        start, end = 0, len(needle)-1
        while end < len(haystack):
            if needle==haystack[start:end+1]:
                return start
            start+=1
            end+=1
        
        return -1