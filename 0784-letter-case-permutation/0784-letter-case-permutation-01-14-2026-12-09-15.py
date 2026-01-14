class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        path = []
        ans = []
        n = len(s)

        def dfs(i):
            if i == n:
                ans.append("".join(path))
                return ans
            c = s[i]
            if c.isalpha():
                path.append(c.upper())
                dfs(i+1)
                path.pop()
                path.append(c.lower())
                dfs(i+1)
                path.pop()            
            else:
                path.append(c)
                dfs(i+1)
                path.pop()   
        dfs(0)
        return ans     


# "a1b2c"
# "A1b2C", "A1B2c"
# cur step: decide lowercase, uppercase on s[i]
# next sub step: decide lowercase, upsercase on s[i+1]
# ....sub step next s[i+2]

#         a,          A
#    a1b    a1B       A1b     A1B
#