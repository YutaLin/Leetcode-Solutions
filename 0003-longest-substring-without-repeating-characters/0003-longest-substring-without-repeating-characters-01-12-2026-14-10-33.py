class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        left = 0
        c_set = set()
        for right, c in enumerate(s):
            while c in c_set:
                c_set.remove(s[left])
                left += 1
            c_set.add(c)

            length = max(length, right - left + 1)

        return length