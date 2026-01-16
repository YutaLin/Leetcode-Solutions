class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        path = []
        ans = []
        n = len(s)

        def dfs(i):
            if len(path) == n:
                ans.append("".join(path))
                return

            c = s[i]
            if c.isdigit():
                path.append(c)
                dfs(i+1)
                path.pop()
            else:
                path.append(c.lower())
                dfs(i+1)
                path.pop()
                path.append(c.upper())
                dfs(i+1)
                path.pop()
        dfs(0)
        return ans

# isDigit
# isChar -> lowercase
#        -> uppercase
