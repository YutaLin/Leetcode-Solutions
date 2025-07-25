# Last updated: 7/24/2025, 8:22:35 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        last = nums[right]

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= last:
                right = mid - 1
            else:
                left = mid + 1
        
        rotation_point = left
        if target == nums[rotation_point]:
            return rotation_point
        elif rotation_point == 0 or target >= nums[0]:
            # Target is in the left section [0, rotation_point-1]
            # Also handle case where array is not rotated (rotation_point == 0)
            left = 0
            right = rotation_point - 1 if rotation_point > 0 else len(nums) - 1
        else:
            # Target is in the right section [rotation_point, len(nums)-1]
            left = rotation_point
            right = len(nums) - 1
        
        # Step 3: Standard binary search in the chosen section
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:   # Fixed: correct direction
                left = mid + 1
            else:
                right = mid - 1
        return -1
                
        