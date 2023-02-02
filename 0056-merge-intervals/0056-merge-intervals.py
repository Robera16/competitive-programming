class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
            
        start=0
        end=1
        result=[]
        n=len(intervals) 
        temp=intervals[0][1]
        
        while(end < n):
            if temp > intervals[end][0] and temp > intervals[end][1]:
                end+=1
            elif temp >= intervals[end][0]:
                temp=intervals[end][1]
                intervals[start][1]=temp 
                end+=1
            else:
                result.append(intervals[start])
                temp=intervals[end][1]
                start=end
                end+=1
                
        result.append(intervals[start])
        
        return result