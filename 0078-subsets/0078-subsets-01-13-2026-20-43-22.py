class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        cur = []
        ans = []
        def dfs(i):
            if i == n:
                ans.append(cur.copy())
                return
            dfs(i+1)
            
            cur.append(nums[i])
            dfs(i+1)
            cur.pop()
        dfs(0)
        return ans

# current operate: enumerate i number choose / not choose
# sub problem: get set from the number of the position larger than i
# next sub problem: get set from the number of the position larger than i + 1


# [1, 2, 3]
#      [],              [1]
#.    [] [2]        [1]       [1, 2]
#   [] [2][2, 3]  [1][1,3]  [1, 2, 3] 