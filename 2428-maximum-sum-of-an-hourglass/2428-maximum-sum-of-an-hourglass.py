class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        max_sum=0
        row,colm = len(grid),len(grid[0])  
        for m in range(1,row-1): 
            for n in range(1,colm-1):
                max_sum=max(max_sum, grid[m][n]+grid[m-1][n]+grid[m+1][n]+grid[m-1][n-1]+
                grid[m-1][n+1]+grid[m+1][n-1]+grid[m+1][n+1])
        return max_sum
