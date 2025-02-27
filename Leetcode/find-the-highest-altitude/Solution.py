// https://leetcode.com/problems/find-the-highest-altitude

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        sum = 0
        max = 0

        for num in gain:
            sum += num
            if sum > max:
                max = sum

        return max
        