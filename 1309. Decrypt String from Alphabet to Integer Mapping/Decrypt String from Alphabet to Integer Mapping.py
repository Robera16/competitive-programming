class Solution:
    def freqAlphabets(self, s: str) -> str:
        string = ''
        n = len(s)-1
        
        while n >=0:
            if s[n] == '#':
                string += chr(96+int(s[n-2:n]))
                n-=3
            else:
                string += chr(96+int(s[n]))
                n-=1

        return string[::-1]