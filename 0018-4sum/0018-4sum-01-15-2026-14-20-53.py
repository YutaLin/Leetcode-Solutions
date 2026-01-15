class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            res = []

            if not nums:
                return res
            

            if k == 2:
                return twoSum(nums, target)

            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for subset in kSum(nums[i+1:], target - nums[i], k - 1):
                        res.append([nums[i]] + subset)

            return res

        def twoSum(nums: List[int], target: int) -> List[int]:
            l = 0
            r = len(nums) - 1
            res = []
            while l < r:
                sum = nums[l] + nums[r]
                if sum == target:
                    res.append([nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif sum < target or (l > 0 and nums[l] == nums[l - 1]):
                    l += 1
                else: 
                    r -= 1
            return res
                    
        nums.sort()
        return kSum(nums, target, 4)
            

# two sum => sort, 2 pointer
# three sum => for loop, fixed number, find other number use two sum
# four sum => for loop, fixed number, find other number use three sum

