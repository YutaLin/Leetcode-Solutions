# Last updated: 7/17/2025, 11:25:53 PM
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left <= right:
            mid = (left + right) // 2
            hours_take = 0
            for pile in piles:
                hours_take += math.ceil(pile / mid)
            
            if hours_take <= h:
                right = mid - 1
            else:
                left = mid + 1

        return left