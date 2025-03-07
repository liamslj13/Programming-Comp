class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        buy = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                total_profit += prices[i] - buy
                buy = prices[i]

        return total_profit
