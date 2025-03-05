class Solution:
    def numSquares(self, n: int) -> int:
        if n == 0:
            return 0
        squares = [i**2 for i in range(1, 101) if i ** 2 <= n]
        dp = [n+1] * (n+1)
        dp[0] = 0

        for a in range(1, n+1):
            for s in squares:
                if a - s >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-s])

        return dp[n]
        
