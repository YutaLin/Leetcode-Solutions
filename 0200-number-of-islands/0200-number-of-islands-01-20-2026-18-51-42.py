class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        r_len = len(grid)
        c_len = len(grid[0])
        visited = [[False] * c_len for _ in range(r_len)]

        def dfs(i: int, j: int) -> int:
            visited[i][j] = True
            for x, y in (i - 1, j), (i + 1, j), (i, j+1), (i, j-1):
                if 0 <= x < r_len and 0 <= y < c_len and grid[x][y] == "1" and not visited[x][y]:
                    dfs(x, y)

        total_size = 0
        
        for i in range(r_len):
            for j in range(c_len):
                if grid[i][j] == "1" and not visited[i][j]:
                    total_size += 1
                    dfs(i, j)

        return total_size
            
