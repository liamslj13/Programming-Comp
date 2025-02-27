// https://leetcode.com/problems/reverse-vowels-of-a-string

class Solution:
    def reverseVowels(self, s: str) -> str:
        #two pointers
        sL = list(s)
        l, r = 0, len(sL) - 1
        vowels = "aeiou"
        print(sL)
        while l < r:
            if sL[l].lower() in vowels and sL[r].lower() in vowels:
                sL[l], sL[r] = sL[r], sL[l]
                l += 1
                r -= 1
            elif sL[l].lower() in vowels:
                r -= 1
            elif sL[r].lower() in vowels:
                l += 1
            else:
                l += 1
                r -= 1
        
        return "".join(sL)


