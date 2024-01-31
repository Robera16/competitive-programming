class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dct={}
        for i in range(len(arr2)):
            dct[arr2[i]]=i
        
        res = []
        other = []
        output = []
        for ele in arr1:
            if ele in dct:
                res.append([ele, dct[ele]])
            else:
                other.append(ele)
        
        sorted_lst = sorted(res, key=lambda x: x[1])
        # print(sorted_lst)
        for lst in sorted_lst:
            output.append(lst[0])
            
        other.sort()
        output.extend(other)
        return output
        
        
        
        