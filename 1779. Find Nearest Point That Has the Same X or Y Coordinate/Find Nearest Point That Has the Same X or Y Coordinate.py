class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        dct = {} # distance as value, index as value key
        valid = False
        for index, coordinate in enumerate(points):
            if coordinate[0]==x or coordinate[1]==y:
                dct[index] = abs(x - coordinate[0]) + abs(y - coordinate[1])
                valid = True
        if valid:
            sort_by_key = dict(sorted(dct.items(),key=lambda item:item[1]))
            return next(iter(sort_by_key))
        else:
            return -1