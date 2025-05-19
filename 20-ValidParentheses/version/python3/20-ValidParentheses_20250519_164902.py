# Last updated: 5/19/2025, 4:49:02 PM
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        for c in s:
            if c in map:
                if len(stack) == 0 or stack.pop() != map[c]:
                    return False
            else:
                stack.append(c)
                
        return len(stack) == 0
        