class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs, key=len)
        temp = strs[0]
        length=len(strs[0])
        for element in strs:
            while(temp[0:length]!=element[0:length]):
                length-=1
        return temp[0:length]
                