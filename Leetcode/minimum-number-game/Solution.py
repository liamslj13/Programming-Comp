// https://leetcode.com/problems/minimum-number-game

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i % 2 == 0:
                result.append(nums[i+1])
            else:
                result.append(nums[i-1])

        return result