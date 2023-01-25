class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        row = len(strs)
        colm = len(strs[0])
        arr = [[]*row for i in range(colm)]
        output=0
        for row in strs:
            for indx,colm in enumerate(row):
                arr[indx].append(colm)

        for row in arr:
            if row != sorted(row):
                output+=1
        return output