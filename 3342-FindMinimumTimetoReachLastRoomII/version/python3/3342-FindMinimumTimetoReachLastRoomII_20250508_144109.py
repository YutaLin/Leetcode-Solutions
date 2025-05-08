# Last updated: 5/8/2025, 2:41:09 PM
# 1. user dijkstra's algorithm to find shortest path
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        if not moveTime:
            return -1
        r = len(moveTime)
        c = len(moveTime[0])
        dp = [[float('inf')] * c for _ in range(r)]
        min_heap = []
        heapq.heappush(min_heap, (0, 0, 0, True))
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while min_heap:
            (cur_time, row, col, is_one_move) = heapq.heappop(min_heap)
            if (row, col) == (r - 1, c - 1):
                return cur_time
            for (d_r, d_c) in directions:
                next_r = row + d_r
                next_c = col + d_c
                move_cost = 1 if is_one_move else 2
                if 0 <= next_r < r and 0 <= next_c < c and dp[next_r][next_c] == float('inf'):
                    next_t = max(moveTime[next_r][next_c], cur_time) + move_cost
                    heapq.heappush(min_heap, (next_t, next_r, next_c, not is_one_move))
                    dp[next_r][next_c] = next_t
        return -1

# move time [[0, 3], [1, 2]]
# (0, 0) -> (1, 0) time: 1 -> 2
# (1, 0) -> (1, 1) time: 2 -> 3

# (0, 0) -> (0, 1) time: 3 + 1 = 4
# (0, 1) -> (1, 1) tiem: 4 > 2 => 4 + 1, 5