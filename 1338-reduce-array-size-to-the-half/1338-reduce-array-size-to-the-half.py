class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arr.sort()
        dct={}
        stack=[]
        stack.append(arr[0]) 
        val=count=1
        while(val < len(arr)):
            if stack[-1]==arr[val]:
                count+=1
            else:
                dct[stack[-1]]=count
                count=1
                stack.append(arr[val])
            val+=1
        dct[stack[-1]]=count
        dct=sorted(dct.items(),key= lambda x:x[1], reverse=True)
        val=dct[0][1]
        output=1
        while(val < len(arr)//2):
            val+=dct[output][1]
            output+=1
        return output

            