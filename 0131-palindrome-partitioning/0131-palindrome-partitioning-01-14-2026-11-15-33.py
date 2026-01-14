class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path = []
        ans = []
        n = len(s)

        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return

            for j in range(i, n):
                t = s[i:j+1]
                if t == t[::-1]:
                    path.append(t)
                    dfs(j+1)
                    path.pop()
        dfs(0)
        return ans
# aab
# a,a,b
#                a 
#   a,     a,        aa,      aab
# a,a,b   a,ab       aa,b

# cur step: s[i...j] path
# next sub step: construct next possible palindrom partition sets from s[j...]
# 