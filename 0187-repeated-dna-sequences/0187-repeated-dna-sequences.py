class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        myMap = {}
        mySet = set()

        for i in range(len(s) - 9):
            if s[i:i+10] in myMap:
                mySet.add(s[i:i+10])
            else:
                myMap[s[i:i+10]] = 1
        
        return mySet