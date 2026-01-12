class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        left = 0
        right = n - 1
        left_most = 0
        right_most = 0
        
        while left <= right:
            left_most = max(left_most, height[left])
            right_most = max(right_most, height[right])
            if left_most < right_most:
                ans += left_most - height[left]
                left += 1
            else:
                ans += right_most - height[right]
                right -= 1
        return ans


# left[i]: max height from left side to [i]

