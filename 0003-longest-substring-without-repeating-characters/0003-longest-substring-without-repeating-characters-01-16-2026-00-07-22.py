class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        l = 0
        longest_sub = 0

        for r, char in enumerate(s):
            if char in char_map and char_map[char] >= l:
                l = char_map[char] + 1
            char_map[char] = r
            longest_sub = max(longest_sub, r - l + 1)

        return longest_sub 