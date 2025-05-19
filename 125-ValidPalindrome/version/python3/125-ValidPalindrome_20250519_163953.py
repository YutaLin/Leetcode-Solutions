# Last updated: 5/19/2025, 4:39:53 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        head_idx = 0
        tail_idx = len(s) - 1

        while head_idx < tail_idx:
            while head_idx < tail_idx and not s[head_idx].isalnum():
                head_idx += 1
            while head_idx < tail_idx and not s[tail_idx].isalnum():
                tail_idx -= 1

            if s[head_idx] != s[tail_idx]:
                return False

            head_idx += 1
            tail_idx -= 1
        return True