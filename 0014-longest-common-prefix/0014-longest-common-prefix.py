class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        temp = strs[0]
        for c in strs:
            while temp != c[:len(temp)] and temp!="":
                temp=temp[:-1]
                
        return temp