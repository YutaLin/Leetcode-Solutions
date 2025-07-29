# Last updated: 7/28/2025, 9:23:40 PM
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        l = 0
        r = len(nums) - 1

        while l <= r: 
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return True

            if nums[l] < nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[l] > nums[mid]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                l = l + 1

        return False





# [1, 2, 3, 4, 4, 4, 5, 6], 0 -> False
# [2, 2, 3, 4, 5, 0, 2, 2], 2 -> True

# [1, 2, 3, 4, 4, 5, 6]
# [2, 3, 4, 5, 6, 0, 1]
# [1, 1, 1, 1, 3, 1] mid == left -> left 