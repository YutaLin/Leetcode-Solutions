# Last updated: 7/21/2025, 9:33:40 PM
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        res = nums[0]
        while left <= right:
            mid = (left + right) // 2
            res = min(res, nums[mid])

            if nums[mid] < nums[len(nums) - 1]:
                right = mid - 1
            else:
                left = mid + 1
        return res