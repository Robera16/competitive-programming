class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output=[]
        urb=0                
        lrb=len(matrix)-1   
        ltb=0
        rtb=len(matrix[0])-1
        x=0
        while(urb<=lrb):
            if lrb<urb or rtb<ltb:
                break
            while(x<=rtb):
                output.append(matrix[urb][x])
                matrix[urb][x]=101
                x+=1
            urb+=1
            x=0
            while(x<=lrb):
                output.append(matrix[x][rtb])
                matrix[x][rtb]=101
                x+=1
            x=rtb
            rtb-=1
            while(x>=ltb):
                output.append(matrix[lrb][x])
                matrix[lrb][x]=101
                x-=1
            x=lrb
            lrb-=1
            while(x>=urb):
                output.append(matrix[x][ltb])
                matrix[x][ltb]=101
                x-=1
            x=0
            ltb+=1
        i=0
        while i < len(output):
            if output[i]==101:
                output.pop(i)
                i-=1
            else:
                i+=1
       
        return output