class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cur = [0] * 26
        for c in s:
            cur[ord(c) - ord('a')] += 1
        for c in t:
            cur[ord(c) - ord('a')] -= 1

        for c in cur:
            if c != 0:
                return False

        return True