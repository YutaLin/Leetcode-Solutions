# Last updated: 7/16/2025, 10:38:55 PM
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square == x:
                return mid
            if square > x:
                right = mid - 1
            else:
                left = mid + 1
        return right