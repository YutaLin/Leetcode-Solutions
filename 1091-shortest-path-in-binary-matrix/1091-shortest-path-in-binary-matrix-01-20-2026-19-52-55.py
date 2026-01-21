class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] != 0:
            return -1
        m = len(grid)
        n = len(grid[0])
        dis = [[-1] * n for _ in range(m)] 

        q = deque([(0, 0)])
        dis[0][0] = 1

        while q:
            i, j = q.popleft()
            for x, y in (i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1), (i-1, j-1), (i + 1, j + 1), (i - 1, j + 1), (i + 1, j - 1):
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 0 and dis[x][y] == -1:
                    dis[x][y] = dis[i][j] + 1
                    
                    if x == m - 1 and y == n - 1:
                        return dis[x][y]
                    q.append((x, y)) 
      
        return -1
# 100
# 110
# 110