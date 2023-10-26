from sortedcontainers import SortedList
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        ans = []
        for i in range(len(searchWord)):
            while products and (i > len(products[0]) - 1 or searchWord[i] != products[0][i]):
                products.pop(0)
            while products and (i > len(products[-1]) - 1 or searchWord[i] != products[-1][i]):
                products.pop()
            ans.append(products[:3])
        # print(ans)
        return ans