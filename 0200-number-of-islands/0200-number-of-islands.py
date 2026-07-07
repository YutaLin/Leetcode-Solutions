class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        r_l = len(grid)
        c_l = len(grid[0]) if r_l > 0 else 0
        
        q = deque()
        for r in range(r_l):
            for c in range(c_l):

                if grid[r][c] == '1':
                    q.append((r, c))
                    grid[r][c] = '0'

                    while q:
                        cur_r, cur_c = q.pop()
                        for nr, nc in [(cur_r+1, cur_c), (cur_r-1,cur_c), (cur_r, cur_c-1), (cur_r, cur_c+1)]:
                            if 0 <= nr < r_l and 0 <= nc < c_l and grid[nr][nc] == '1':
                                q.append((nr, nc))
                                grid[nr][nc] = "0"    
                            
                                    
                    ans += 1

        return ans