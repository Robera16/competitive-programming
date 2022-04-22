class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        original=[]
        changed.sort()
        
        if (len(changed) %2!=0):
            return []
        Op=0
        Dp=1
        while(Dp < len(changed)):
            if changed[Dp]==2*changed[Op]:
                original.append(changed[Op])
                changed[Dp]=-1
                Dp+=1
                Op+=1
            elif changed[Op]==-1:
                Op+=1
                if Dp==Op:
                    Dp+=1
            else:
                Dp+=1
        if len(changed)!=2*len(original):
            return []
        return original