class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        start, k=0, len(p)
        sHeap, pHeap=[0]*26, [0]*26
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
        