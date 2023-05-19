class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        dct={}
        for i in range(n):
            dct[i]=True
        
        for lst in edges:
            dct[lst[1]]=False
        
        output = []
        for key, value in dct.items():
            if value==True:
                output.append(key)
                
        return output
            