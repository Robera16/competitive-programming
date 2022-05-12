class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # position                         0, 3, 5, 8, 10
        # speed                            1, 3, 1, 4, 2
        # target(12)-position / speed      12,3, 7, 1, 1    hours to reach destination   
        # output                           12, (3,7), (1,1) 
        # stack content         12 then 12, 3 then 12,7 then 12,7,1 then 12, 7, 1 so len=3
        # required HR for car at position 0 never be less than the rest if less
        # add 1 to the fleet
        
        # 0,  2,  4
        # 4,  2,  1
        # 25, 49, 96
        # (25, 49, 96)
        # stack content 25 then 49 then 96 so len=1
        
        pws=[]
        n=len(position)
        for x in range(n):
            pws.append((position[x], speed[x]))
        
        pws.sort()
        Hrs=[]
        for x in range(n):
            Hrs.append((target-pws[x][0])/pws[x][1])
        
        stack=[]
        for x in Hrs:
            if len(stack):
                if x >= stack[-1]:
                    while(len(stack) and x >= stack[-1]):
                        stack.pop()
            stack.append(x)  
        return len(stack)
    
        