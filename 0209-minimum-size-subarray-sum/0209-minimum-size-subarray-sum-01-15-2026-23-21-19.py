class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        n = len(nums)
        min_len = n + 1
        s = 0
        for r, num in enumerate(nums):
            s += num
            
            while s >= target:
                min_len = min(r - l + 1, min_len)
                s -= nums[l]
                l += 1
        
        return min_len if min_len <= n else 0
