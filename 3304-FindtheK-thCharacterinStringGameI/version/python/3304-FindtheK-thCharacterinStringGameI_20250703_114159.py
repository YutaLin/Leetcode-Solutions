# Last updated: 7/3/2025, 11:41:59 AM
class Solution:
    def kthCharacter(self, k: int) -> str:
        word = 'a'
        while len(word) < k:
            concatenate = ''
            for c in word:
                concatenate += chr(ord(c) + 1)
            word += concatenate
        return word[k-1]