class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dct={}
        for match in matches:
            if match[0] in dct:
                dct[match[0]] = dct[match[0]] + 0
            else:
                dct[match[0]] = 0
            if match[1] in dct:
                dct[match[1]] = dct[match[1]] + 1
            else:
                dct[match[1]] = 1

        dct = dict(sorted(dct.items(), key = lambda x:x[0]))

        output = [[],[]]
        for key, value in dct.items():
            if value == 0:
                output[0].append(key)
            if value == 1:
                output[1].append(key)
        return output