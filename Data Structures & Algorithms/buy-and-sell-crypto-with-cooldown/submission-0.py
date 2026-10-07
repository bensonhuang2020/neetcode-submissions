class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # each day, we can take 2 actions depending on our state. considering a fresh state, we can either buy or not buy. if we own a coin, the next day we can either sell, then have to skip a day or hold.
        n = len(prices)
        memo = {}
        def trade(i, holding = False):
            if (i, holding) in memo:
                return memo[(i, holding)]
            if i >= n:
                return 0
            
            if not holding:
                memo[(i, holding)] = max(-prices[i] + trade(i + 1, True), trade(i + 1))
            else:
                memo[(i, holding)] = max(prices[i] + trade(i + 2, False), trade(i + 1, holding))
            return memo[(i, holding)]


        # when we call, it's presumed that we're not holding or purchased anything
        return max(-prices[0] + trade(1, True), trade(1, False))