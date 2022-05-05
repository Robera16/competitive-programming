class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h_index=1
        for i in citations:
            if i>=h_index:
                h_index+=1
            else:
                break 
        return h_index-1