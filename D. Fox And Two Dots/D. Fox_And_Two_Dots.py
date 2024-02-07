def is_valid_cell(x, y, n, m):
    # Check if the cell coordinates (x, y) are within the bounds of the board.
    return 0 <= x < n and 0 <= y < m

def dfs(board, visited, color, x, y, px, py):
    # Mark the current cell as visited.
    visited[x][y] = True

    # Check all four adjacent cells.
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy

        # Skip if the adjacent cell is the previous cell or out of bounds.
        if nx == px and ny == py or not is_valid_cell(nx, ny, len(board), len(board[0])):
            continue

        # Check if the adjacent cell has the same color and is already visited.
        if is_valid_cell(nx, ny, len(board), len(board[0])) and board[nx][ny] == color and visited[nx][ny]:
            return True

        # If the adjacent cell has the same color and is not visited, perform DFS on it.
        if is_valid_cell(nx, ny, len(board), len(board[0])) and board[nx][ny] == color and not visited[nx][ny]:
            if dfs(board, visited, color, nx, ny, x, y):
                return True

    # No cycle found, backtrack and mark the current cell as unvisited.
    visited[x][y] = False
    return False

def has_cycle(board):
    n, m = len(board), len(board[0])
    visited = [[False] * m for _ in range(n)]

    # Iterate through all cells in the board.
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                if dfs(board, visited, board[i][j], i, j, -1, -1):
                    return True

    return False

# Read input
n, m = map(int, input().split())
board = [input() for _ in range(n)]

# Check if there exists a cycle
if has_cycle(board):
    print("Yes")
else:
    print("No")