class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strr=''
        for char in digits:
            strr+=str(char)
        
        num = int(strr)+1
        result=[]
        for char in str(num):
            result.append(int(char))
        return result