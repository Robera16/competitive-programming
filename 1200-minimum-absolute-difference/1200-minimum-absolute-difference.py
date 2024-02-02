class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # find minimum absolute difference
        min_value = float('inf')
        arr.sort()
        output=[]
        for i in range(len(arr)-1):
            min_value = min(min_value, arr[i+1]-arr[i])
        
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]==min_value:
                output.append([arr[i], arr[i+1]])
                
        return output