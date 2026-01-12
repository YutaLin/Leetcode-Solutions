class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n + 1
        s = 0
        left = 0
        for i in range(n):
            s += nums[i]
            while s - nums[left] >= target:
                s -= nums[left]
                left += 1

            if s >= target:
                ans = min(i - left + 1, ans)

        return ans if ans <= n else 0