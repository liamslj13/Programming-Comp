// https://leetcode.com/problems/plus-one

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for n in digits:
            num += str(n)
        num = int(num) + 1
        res = []
        for c in str(num):
            res.append(int(c))

        return res
        