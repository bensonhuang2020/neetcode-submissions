class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        """
        # bad solution since we're doing n^2
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                max_profit = max(max_profit, prices[j]-prices[i])
        return max_profit
        """
        lowest_price = prices[0]
        for i in range(len(prices)):
            max_profit = max(max_profit, prices[i] - lowest_price)
            lowest_price = min(lowest_price, prices[i])
        return max_profit