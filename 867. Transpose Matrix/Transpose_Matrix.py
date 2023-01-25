class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        colm = len(matrix[0])
        output = [[]*row for i in range(colm)]
        for row in matrix:
            for indx,colm in enumerate(row):
                output[indx].append(colm)

        return output