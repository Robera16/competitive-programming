class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aval,bval=0,0
        for index,val in enumerate(a[::-1]):
            aval+= (pow(2,index)*int(val))
        
        for index,val in enumerate(b[::-1]):
            bval+= (pow(2,index)*int(val))
        
        return bin(aval+bval)[2:]
            
            