class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        list=[]
        list2=[]
        dct={}
        i=0
        
        for word in strs:
            temp=(''.join(sorted(word)))
            dct[i]= temp
            list.append(temp)
            i+=1
        
        dct2=dict(sorted(dct.items(),key= lambda x:x[1]))
        list.sort()
        
        unique_list = []
        for x in list:       
            if x not in unique_list:
                unique_list.append(x)
                  
        for key,value in dct2.items():
            if value==unique_list[0]:
                result.append(strs[key])
            else:
                unique_list.remove(unique_list[0])
                list2.append(result)
                result=[]
                result.append(strs[key])
        list2.append(result)
        return list2