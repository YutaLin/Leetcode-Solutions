class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx = {}
        for idx, num in enumerate(nums):
            need = target - num
            if need in num_idx:
                return [idx, num_idx[need]]
            
            num_idx[num] = idx

        return [-1, -1]



# loop each number
# subtract cur value and find if it in dic
# if yes -> return value
# if no -> put number in dic and continue
