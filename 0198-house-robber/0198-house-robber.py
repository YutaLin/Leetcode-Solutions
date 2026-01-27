class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # dp = [0] * (n + 2)
        newF = 0
        for i, x in enumerate(nums):
            # dp[i+2] = max(dp[i+1], dp[i] + nums[i])

# f(i) = max(f(i-1), f(i-2) + nums[i])

        return dp[n+1]
        f0 = 0
        f
# 
