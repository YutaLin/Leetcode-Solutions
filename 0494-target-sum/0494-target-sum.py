    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target += sum(nums)

        if target < 0 or target % 2 != 0:
            return 0
        target //= 2
        # n = len(nums)

# p - (s - p) = t
# 2p = s + t
# p = (s + t) / 2

        f = ji

        for x in nums:
            for c in range(target+1):
                if c < x:
                    dp[i+1][c] = dp[i][c]
                else:
                    dp[i+1][c] = dp[i][c] + dp[i][c-x]

        return dp[n][target]

class Solution:
