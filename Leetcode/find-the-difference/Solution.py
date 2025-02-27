// https://leetcode.com/problems/find-the-difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sA = list(s)
        tA = list(t)

        sA.sort()
        tA.sort()

        for i in range(len(sA)):
            if sA[i] != tA[i]:
                return tA[i]
        

        return tA[len(tA)-1]