class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cst = sorted(cost, reverse=True)
        total_cost, count = sum(cst), 1
        
        for i in range(len(cost)):
            if count==3:
                total_cost-=cst[i]
                count=1
            else:
                count+=1
                
        return total_cost
        