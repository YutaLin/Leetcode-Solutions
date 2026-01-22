class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        if not rooms:
            return
        
        rows = len(rooms)
        cols = len(rooms[0])

        visited = set()
        q = deque([])
        
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))

        while q:
            q_len = len(q)
            for i in range(q_len):
                r, c = q.popleft()
                for x, y in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                    if (min(x, y) < 0 or x == rows or y == cols or
                            (x, y) in visited or rooms[x][y] == -1):
                            continue
                    rooms[x][y] = rooms[r][c] + 1
                    visited.add((x, y))
                    q.append((x, y))

        return rooms
                
