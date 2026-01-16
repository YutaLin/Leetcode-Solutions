class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0

        s = 1
        res = 0
        l = 0

        for r, num in enumerate(nums):
            s *= num           
            while s >= k:
                s /= nums[l]
                l += 1
            res += r - l + 1

        return res

# nums[i:j] < k, how many?
# numbers: positive?
# nums[i] postive <

# [1, 2, 3, 4, 2, 1] 10
#        l, r