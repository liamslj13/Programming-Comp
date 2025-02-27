// https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = "qwertyuioopasdfghjklzxcvbnm1234567890"
        build = []

        for char in s.lower():
            if char in letters:
                build.append(char)
        
        return build == build[::-1]
        
                
