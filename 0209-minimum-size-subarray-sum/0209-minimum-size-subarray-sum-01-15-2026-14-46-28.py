class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum = 0
        n = len(nums)
        l = 0
        min_length = n + 1

        for r, num in enumerate(nums):
            sum += num
            
            while sum - nums[l] >= target:
                sum -= nums[l]
                l += 1

            if sum >= target:
                min_length = min(min_length, r - l + 1)
        
        return min_length if min_length <= n else 0
                

# sum number till > target

# [2, 3, 1, 2, 4, 3]
# l         r       sum all number >= target stop
#    l              move l till sum < target
#.             r  
#.      l 