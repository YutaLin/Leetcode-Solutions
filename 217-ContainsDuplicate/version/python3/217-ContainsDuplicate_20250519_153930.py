# Last updated: 5/19/2025, 3:39:30 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_num = set()
        for num in nums:
            if num in set_num:
                return True
            else:
                set_num.add(num)
        return False