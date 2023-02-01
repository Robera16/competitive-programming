class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        output=[]
        count=len(arr2)
        dct={}
        for index, val in enumerate(arr2):
            dct[val] = index
            
        for value in arr1:
            if value in dct:  
                output.append([value, dct[value]])
            else:
                output.append([value, count+value])
                
        sorted_nested = sorted(output, key=lambda x: x[1])
        return [i[0] for i in sorted_nested]