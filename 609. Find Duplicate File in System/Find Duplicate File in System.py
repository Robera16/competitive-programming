class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dct={}
        output=[]
        for path in paths:
            cont = path.split()
            for x in cont[1:]:
                start = x.find("(")
                end = x.find(")")
                if x[start+1:end] in dct:
                    dct[x[start+1:end]].append(cont[0]+'/'+ x[:start])
                else:
                    dct[x[start+1:end]] = [cont[0]+'/'+ x[:start]]

        for key, value in dct.items():
            if len(value) > 1:
                output.append(value)
                
        return output
            