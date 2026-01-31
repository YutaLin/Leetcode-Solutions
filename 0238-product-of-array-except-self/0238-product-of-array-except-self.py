class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        pre = 1

        for i in range(len(nums)-1):
            pre *= nums[i]
            output[i+1] *= pre
        
        pre = 1
        for i in range(len(nums)-1, 0, -1):
            pre *= nums[i]
            output[i-1] *= pre

        return output

# [1, 2, 3, 4]
#
# [1, 1, 1, 1]
#  prefix = 1
#  
# for loop nums and product put to index + 1
# 