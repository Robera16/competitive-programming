class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        best = score = sum(cardPoints[:k])
        print('best-score', best)
        for i in range(1, k+1):
            score = score - cardPoints[k-i] + cardPoints[-i]
            best = score if score > best else best
            print('score', score, 'best', best)
            
        return best