// https://leetcode.com/problems/maximum-sum-with-at-most-k-elements

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        maxVals = []
        for i in range(len(grid)):
            grid[i].sort()
            descending = grid[i][::-1]
            take = min(limits[i], len(descending))
            maxVals.extend(descending[:take])
        
        maxVals.sort()
        maxVals = maxVals[::-1]
        
        return sum(maxVals[:k])