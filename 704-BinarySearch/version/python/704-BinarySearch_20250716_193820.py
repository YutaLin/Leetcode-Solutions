# Last updated: 7/16/2025, 7:38:20 PM
# In the end, we only need to check if all number less than target, so we should check left index.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

        if left < len(nums) and nums[left] == target:
            return left
        
        return -1



# [-3, -1, 2, 6, 10]: 
# target -1, -> 1
# target 0 -> -1