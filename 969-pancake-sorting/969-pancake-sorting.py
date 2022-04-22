class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        output=[]
        validRange=len(arr)
        
        while(validRange):
            k=arr.index(max(arr[0:validRange]))+1
            output.append(k)
            arr[0:k]=reversed(arr[0:k])
            arr[0:validRange]=reversed(arr[0:validRange])
            output.append(validRange)
            validRange-=1
        
        print(arr)
        return output
            