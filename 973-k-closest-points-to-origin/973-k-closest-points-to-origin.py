class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        answer=[]
        output=[]
        index=0
        for point in points:
            answer.append((sqrt(pow(point[0], 2) + pow(point[1], 2)), index ))
            index+=1
        
        if answer:
            answer.sort()
            for i in range(k):
                output.append(points[answer[i][1]])
        
        return output
        
        