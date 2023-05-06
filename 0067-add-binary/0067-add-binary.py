class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aVal, bVal = 0, 0
        i = 0
        for char in a[::-1]:
            aVal += (pow(2,i)*int(char))
            i+=1
        
        i = 0
        for char in b[::-1]:
            bVal += (pow(2,i)*int(char))
            i+=1
            
        return bin(aVal+bVal)[2:]
            
            