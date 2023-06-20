class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # direction vectors
     
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        # perimeter = 0
        direction_vector = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def is_valid_cell(x, y, n, m):
            return 0 <= x < n and 0 <= y < m
        
        
        def dfs(grid, visited, perimeter, x, y):
            visited[x][y] = True
            if grid[x][y]==1:
                for dx, dy in direction_vector:
                    nx, ny = x + dx, y + dy
 
                    if is_valid_cell(nx, ny, len(grid), len(grid[0])) and grid[nx][ny]==0:
                        perimeter+=1
                    if not is_valid_cell(nx, ny, len(grid), len(grid[0])):
                        perimeter+=1
           
            for dx, dy in direction_vector:
                nx, ny = x + dx, y + dy
                if is_valid_cell(nx, ny, len(grid), len(grid[0])) and not visited[nx][ny]:
                    return dfs(grid, visited, perimeter, nx, ny)
                    
            return perimeter                 
             

        return dfs(grid,visited, 0, 0, 0)
        
        