// https://leetcode.com/problems/move-zeroes

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                for j in range(len(nums)):
                    if i + j >= len(nums):
                        break
                    if nums[i+j] != 0:
                        nums[i] = nums[i+j]
                        nums[i+j] = 0
                        break

    
        