class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        start=0
        sHeap=[0]*26
        pHeap=[0]*26
        k=len(p)
        output=[]
        for c in p:
            pHeap[ord(c)-ord('a')]+=1
            
        for i in range(len(s)):
            sHeap[ord(s[i])-ord('a')]+=1
            if ((i-start+1)==k):
                if pHeap==sHeap:
                    output.append(start)
                sHeap[ord(s[start])-ord('a')]-=1
                start+=1
                
        return output
        