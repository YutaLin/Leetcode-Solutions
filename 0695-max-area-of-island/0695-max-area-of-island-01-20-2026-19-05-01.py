class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        r_len = len(grid)
        c_len = len(grid[0])
        visited = [[False] * c_len for _ in range(r_len)]

        def dfs(i: int, j: int) -> int:
            visited[i][j] = True
            size = 1
            for x, y in (i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1):
                if 0 <= x < r_len and 0 <= y < c_len and not visited[x][y] and grid[x][y] == 1:
                    size += dfs(x, y)
            return size

        max_size = 0
        for i, row in enumerate(grid):
            for j, ch in enumerate(row):
                if ch != 1 or visited[i][j]:
                    continue
                size = dfs(i, j)
                max_size = max(max_size, size)
        return max_size
            