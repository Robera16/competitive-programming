class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        def pascal(k, lst):
            if k==rowIndex:
                return lst
            
            copy=[]
            copy.append(1)
            k+=1
            n=k-1
            i=1
            while n:
                copy.append(lst[i-1]+lst[i])
                n-=1
                i+=1
                
            copy.append(1)
            return pascal(k,copy)
            
        return pascal(0,[1])
            
            
            
            