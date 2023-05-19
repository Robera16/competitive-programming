class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        dct = {}
        for lst in edges:
            for ele in lst:
                if ele in dct:
                    dct[ele]+=1
                else:
                    dct[ele]=1
        
        sort_by_value = dict(sorted(dct.items(), key=lambda item: item[1], reverse=True))
        
        first_value = list(sort_by_value)[0]
        # print(len(edges))
        # print(dct)
        # print(sort_by_value)
        return first_value
        