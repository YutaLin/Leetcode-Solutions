class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        ans = 0
        while l < r:
            ans = max(ans, min(height[l], height[r]) * (r - l))
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return ans
        

# [1, 2, 2, 1] -> 3
# [1, 2, 2, 2, 1] -> 4
# [1,1] -> 1
# [5,1] -> 1