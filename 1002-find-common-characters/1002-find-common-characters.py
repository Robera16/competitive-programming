class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        dct={}
        output=[]
        i=1
        for char in list(set(words[0])):
            dct[char]=words[0].count(char)
       
        while (i < len(words)):
            for char, value in dct.items():
                cnt=words[i].count(char)
                if  cnt < value:
                    dct[char]=cnt
            i+=1
        
        for char, value in dct.items():
            output+=[char]*value

        return output
