class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        output=[]
        count=len(arr2)
        for value in arr1:
            if value in arr2:
                output.append([value, arr2.index(value)])
            else:
                output.append([value, count+value])
                
        
        sorted_nested = sorted(output, key=lambda x: x[1])
        answer=[]
        for lst in sorted_nested:
            answer.append(lst[0])
        return answer