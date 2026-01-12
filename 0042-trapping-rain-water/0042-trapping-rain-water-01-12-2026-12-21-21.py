class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_most = [0] * n
        right_most = [0] * n

        max_left = 0
        for i in range(n):
            max_left = max(max_left, height[i])
            left_most[i] = max_left

        max_right = 0
        for i in range(n - 1, -1, -1):
            max_right = max(max_right, height[i])
            right_most[i] = max_right

        trap_water = 0
        for i in range(n):
            cur_trap = (min(right_most[i], left_most[i]) - height[i]) * 1
            trap_water += cur_trap
        return trap_water

# left[i]: max height from left side to [i]

