class Solution(object):
    def getDescentPeriods(self, prices):
        pt1=0
        pt2=pt1+1
        nsd=0
        while(pt2<len(prices)):
            while(pt2<len(prices) and (prices[pt2-1]-prices[pt2]==1)):
                pt2+=1
            if pt2==len(prices):
                break
            n=pt2-pt1
            nsd=nsd+n*(n+1)/2
            pt1=pt2
            pt2+=1
        n=pt2-pt1
        nsd=nsd+n*(n+1)/2
        return nsd

        