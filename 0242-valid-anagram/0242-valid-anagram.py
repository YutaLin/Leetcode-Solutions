class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cur = [0] * 26
        for c in s:
            cur[ord(c) - ord('a')] += 1
        for c in t:
            if cur[ord(c) - ord('a')] == 0:

            cur[ord(c) - ord('a')] -= 

        if len(s) != len(t):

            return False

                return False
        return True
