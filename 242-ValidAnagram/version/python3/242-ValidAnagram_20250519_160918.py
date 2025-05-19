# Last updated: 5/19/2025, 4:09:18 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_char = {}
        for char in s:
            if char in map_char:
                map_char[char] += 1
            else:
                map_char[char] = 1
        
        for char in t:
            if char in map_char:
                map_char[char] -= 1
                if map_char[char] == 0:
                    del map_char[char]
            else:
                return False

        return True