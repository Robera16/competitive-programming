class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix)==1:
            if target in matrix[0]:
                return True
            else:
                return False

        for i in range(len(matrix)-1):
            if matrix[i][0] <= target < matrix[i+1][0]:
                if target in matrix[i]:
                    return True
                else:
                    return False
            else:
                if target in matrix[i+1]:
                    return True