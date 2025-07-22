# Last updated: 7/21/2025, 8:58:53 PM
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = (left + right) // 2
            cur_weight = 0
            cur_days = 0
            for weight in weights:
                if cur_weight + weight <= mid:
                    cur_weight += weight
                else:
                    cur_days += 1
                    cur_weight = weight
            if cur_weight > 0:
                cur_days += 1

            if cur_days <= days:
                right = mid - 1
            else:
                left = mid + 1
        
        return left
        

                