class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dct=defaultdict(int)
        counter=0
        output=0
        start=0
        for i in range(len(s)):
            if s[i] not in dct:
                dct[s[i]]=i
                counter+=1
            else:
                output=max(output,counter)
                if dct[s[i]]+1 > start:
                    start=dct[s[i]]+1
                counter=i-start+1
                dct[s[i]]=i
        return max(output,counter)