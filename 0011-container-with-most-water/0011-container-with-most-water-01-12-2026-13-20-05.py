class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        
        max_water = 0
        while left < right:
            area = (right - left) * min(height[right], height[left])
            max_water = max(max_water, area)
            
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return max_water

# n = 0?
# [1, 2, 3, 4, 5, 4, 2, 1]
#  2*5 = 10
#  2*4 = 8
#  2*3 = 6
#  3*3 = 9
#  4*1 = 4

