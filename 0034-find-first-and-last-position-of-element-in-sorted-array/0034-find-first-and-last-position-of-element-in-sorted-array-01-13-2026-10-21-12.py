class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        

        def bfs(nums, target):
            
            left = 0
            right = n - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] >= target:
                    right -= 1
                else:
                    left += 1
            return left
        first = bfs(nums, target)
        if first < n and nums[first] == target:
            second = bfs(nums, target + 1) - 1
            return [first, second]
        return [-1, -1]





# [1, 2, 3, 4, 5]
# [1, 1, 2, 2, 3]

# [-1, -1, -3]