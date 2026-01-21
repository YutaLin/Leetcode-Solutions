class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        if not maze:
            return -1
        m, n = len(maze), len(maze[0])
        dis = [[-1] * n for _ in range(m)]

        dis[entrance[0]][entrance[1]] = 0
        q = deque([(entrance[0], entrance[1])])

        while q:
            i, j = q.popleft()
            for x, y in (i, j-1), (i, j+1), (i-1, j), (i+1, j):
                if 0 <= x < m and 0 <= y < n and dis[x][y] == -1 and maze[x][y] == ".":
                    dis[x][y] = dis[i][j] + 1
                    if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                        return dis[x][y]
                    q.append((x, y))
        return -1