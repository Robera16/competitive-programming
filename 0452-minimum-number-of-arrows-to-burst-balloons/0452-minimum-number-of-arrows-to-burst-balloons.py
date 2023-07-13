class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        output,i = 0,0
        n=len(points)
        while i<n:
            temp = i+1
            while temp<n and points[i][1]>=points[temp][0]:
                temp+=1
                
            output+=1
            i=temp
        return output