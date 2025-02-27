// https://leetcode.com/problems/kids-with-the-greatest-number-of-candies

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        bools = []
        for i in range(len(candies)):
            bools.append(max(candies)<=candies[i] + extraCandies)

        return bools