// https://leetcode.com/problems/reverse-words-in-a-string

class Solution:
    def reverseWords(self, s: str) -> str:
        sL = s.strip().split(" ")
        print(sL)
        build = []

        for i in range(len(sL)-1, -1, -1):
            if i == 0:
                build.append(sL[i])
            elif sL[i] != '':
                build.append(sL[i])

        return " ".join(build)
                

        

        