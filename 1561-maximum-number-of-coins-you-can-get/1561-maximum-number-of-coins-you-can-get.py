class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        val = len(piles)//3 - 1
        
        if (val==0):
            return piles[1]
        else:
            i=val+1
            val=0
            while(i < len(piles)):
                val+=piles[i]
                i+=2
                
            return val
        