// https://leetcode.com/problems/length-of-last-word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        arr = s.split(" ")
        return len(arr[-1])