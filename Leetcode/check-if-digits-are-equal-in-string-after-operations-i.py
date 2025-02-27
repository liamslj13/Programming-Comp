// https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        digits = []
        for char in s:
            digits.append(int(char))
            
        while len(digits) > 2:
            digitArray = []
            
            for i in range(0,len(digits)-1):
                sum = digits[i] + digits[i+1]
                res = sum % 10
                digitArray.append(res)
            digits = digitArray
        
        if digits[0]==digits[1]:
            return True
        return False