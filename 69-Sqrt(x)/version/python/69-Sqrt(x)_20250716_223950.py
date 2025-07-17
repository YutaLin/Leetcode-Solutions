# Last updated: 7/16/2025, 10:39:50 PM
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left = 2
        right = x // 2
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