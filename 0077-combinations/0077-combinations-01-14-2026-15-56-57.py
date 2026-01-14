class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        ans = []

        def dfs(i):
            if n + 1 - i < k - len(path):
                return
            if len(path) == k:
                ans.append(path.copy())
                return 

            for j in range(i, n+1):
                path.append(j)
                dfs(j+1)
                path.pop()

        dfs(1)
        return ans

# n = 3, k = 2
#    1      2
# 12  13     23

# cur step, we choose number from nums[i..n]
# next sub step, we choose number from numbs[i+1...n]
# count of number we choose is k = 