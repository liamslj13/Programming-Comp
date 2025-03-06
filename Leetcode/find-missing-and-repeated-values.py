class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        sol = {}
        repeat = 0
        yea = 0

        for i in range(len(grid)):
            for j in range(len(grid)):
                sol[grid[i][j]] = 1 + sol.get(grid[i][j], 0)

        arr = []
        for k, v in sol.items():
            arr.append(k)
            if v == 2:
                repeat = k

        arr.sort()
        check = []
        for i in range(len(arr) + 1):
            check.append(i + 1)

        for i in range(len(check)):
            if i == len(arr):
                yea = check[i]
                break
            elif check[i] < arr[i]:
                yea = check[i]
                break

        return [repeat, yea]
