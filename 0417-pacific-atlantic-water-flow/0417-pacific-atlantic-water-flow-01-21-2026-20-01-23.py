class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pac = set()
        atl = set()

        def dfs(r, c, visit, preHeight):
                visit.add((r, c))
                for x, y in (r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1):
                    if (x, y) not in visit and 0 <= x < rows and 0 <= y < cols and heights[x][y] >= preHeight:               
                        
                        dfs(x, y, visit, heights[x][y])

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res