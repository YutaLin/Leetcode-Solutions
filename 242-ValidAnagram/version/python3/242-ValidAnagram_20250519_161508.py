# Last updated: 5/19/2025, 4:15:08 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_char = {}
        for char in s:
            map_char[char] = map_char.get(char, 0) + 1
        
        for char in t:
            if char not in map_char:
                return False
            map_char[char] -= 1
            if map_char[char] == 0:
                del map_char[char]

        return not map_char