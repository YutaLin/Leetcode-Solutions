class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        ans = []

        def dfs(i):        
            if len(path) == k:
                ans.append(path.copy())
                return

            for j in range(i, n+1):
                path.append(j)
                dfs(j+1)
                path.pop()
        dfs(1)
        return ans

# n = 4, k = 2
# 