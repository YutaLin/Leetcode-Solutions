class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = []
        ans = []
        m = n * 2

        def bfs(i, open):
            if i == m:
                ans.append("".join(path))
                return ans

            
            if open < n:
                path.append('(')
                bfs(i+1, open + 1)
                path.pop()
            if i - open < open:
                path.append(')')
                bfs(i+1, open)
                path.pop()         
                
                
        bfs(0, 0)
        return ans
                
# n = 2        
#    (
#  ((  ()    open
# (()) ()()

# cur problem: enumerate path[i] is left or right parenthesis
# sub problem: construct path[> i]
# next sub problem: enumerate path[i+1] is left or right parenthesis

# open: for record left parathensis
# open < n: can select left parathensis
# i - open < open: can select right parathensis


