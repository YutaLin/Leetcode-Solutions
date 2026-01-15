class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def bfs(target, l, r):
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return l
        
        l = 0
        r = len(nums) - 1
        pos_start = bfs(1, 0, r)
        neg_end = bfs(0, 0, r)
        
        return max(neg_end, len(nums) - pos_start)


        
        

# find 0