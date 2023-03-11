class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        index,timeTaken=0, 0
        while tickets[k] > 0:
            
            if tickets[index] > 0:
                tickets[index]-=1
                timeTaken+=1
                
            index+=1
            if index==len(tickets):
                index=0
        
        return timeTaken