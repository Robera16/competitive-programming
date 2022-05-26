class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        for i in range(n-1):
            temp = invert(s)
            s = s+"1"+temp[::-1]
        l=list(s) 
        return l[k-1]
    
def invert(s):
    tem=''
    for i in s:
        if i=='0':
            tem+='1'
        else:
            tem+='0'
    return tem