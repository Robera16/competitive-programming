class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []
        def backtrack(start, lst):
            if len(lst)==k:
                output.append(lst.copy())
                return 
            for i in range(start, n+1):
                lst.append(i)
                backtrack(i+1, lst)
                lst.pop()
        
        backtrack(1, [])
        return output