class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words_dct = {}
        for word in words:
            if word in words_dct:
                words_dct[word]+=1
            else:
                words_dct[word]=1
        
        heap = []
        for word, count in words_dct.items():
            heapq.heappush(heap, (-count, word))
        
        # print(words_dct)
        # print(heap)
       
        # print(heapq.heappop(heap))
        # print(heapq.heappop(heap))
        output = []
        while k > 0:
            output.append(heapq.heappop(heap)[1])
            k-=1
        return output
                