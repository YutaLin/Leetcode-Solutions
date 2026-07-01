class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0]*26

        for sC in s:
            count[ord(sC) - ord('a')] += 1

        for tC in t:
            if count[ord(tC) - ord('a')] == 0:
                return False
            count[ord(tC) - ord('a')] -= 1
        
        for num in count:
            if num != 0:
                return False

        return True