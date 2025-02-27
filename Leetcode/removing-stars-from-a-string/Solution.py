// https://leetcode.com/problems/removing-stars-from-a-string

class Solution:
    def removeStars(self, s: str) -> str:
        # implement a stack
        stack = []
        for char in s:
            if char != '*':
                stack.append(char)
            else:
                stack.pop()
        
        return "".join(stack)