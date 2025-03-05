class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solutions = []

        for i in range(len(nums)):
            l = i + 1
            r = len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while l < r:
                result = nums[i] + nums[l] + nums[r]
                if result == 0:
                    solutions.append([nums[i],nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif result < 0:
                    l += 1
                else:
                    r -= 1

        return solutions
