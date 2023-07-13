class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        output = 0
       
        if numOnes >= k:
            output+=k
        else:
            output+=numOnes
            k-= numOnes
            if numZeros < k:
                k-=numZeros
                if numNegOnes>=k:
                    output-=k
                else:
                    output-=numNegOnes
                
        
        return output
        