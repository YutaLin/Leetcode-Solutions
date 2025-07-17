# Last updated: 7/16/2025, 10:26:43 PM
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            mid = (left + right) // 2
            g = guess(mid)
            if g == 0:
                return mid
            elif g == -1:
                right = mid - 1
            else:
                left = mid + 1
        return -1
        