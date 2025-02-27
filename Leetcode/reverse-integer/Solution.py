// https://leetcode.com/problems/reverse-integer

class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            neg = True
        intstr = str(abs(x))
        if neg:
            string = "-"
            string += str(int(intstr[::-1]))
        else:
            string = str(int(intstr[::-1]))

        if abs(int(string)) > 2**31-1:
            return 0
        return int(string)
