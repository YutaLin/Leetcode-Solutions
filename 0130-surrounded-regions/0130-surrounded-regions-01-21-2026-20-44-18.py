class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows = len(board)
        cols = len(board[0])
        visit = set()

        def dfs(r, c):
            visit.add((r, c))
            for x, y in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                if 0 <= x < rows and 0 <= y < cols and (x, y) not in visit and board[x][y] == 'O':
                    dfs(x, y)
            
            
        for r in range(rows):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][cols - 1] == 'O':
                dfs(r, cols - 1)

        for c in range(cols):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[rows - 1][c] == 'O':
                dfs(rows - 1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r, c) not in visit:
                    board[r][c] = 'X'
        
        return board


# loop around bound
# check if it is '0' and dfs, mark '0' visit
# loop board and flip