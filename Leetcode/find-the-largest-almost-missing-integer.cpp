class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        map = {}

        for i in range(len(nums)-k+1):
            sub = set(nums[i:i+k])
            for num in sub:
                map[num] = 1 + map.get(num, 0)

        num = -1

        for n, c in map.items():
            if c == 1:
                num = max(num, n)
        return num        
