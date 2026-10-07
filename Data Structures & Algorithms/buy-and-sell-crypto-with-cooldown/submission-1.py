class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # each day, we can take 2 actions depending on our state. considering a fresh state, we can either buy or not buy. if we own a coin, the next day we can either sell, then have to skip a day or hold.
        n = len(prices)
        memo = {}

        # memoization happens if we hit the parts where we can buy a coin and we're at a certain index. 
        def trade(i, holding = False):
            if (i, holding) in memo:
                return memo[(i, holding)]
            if i >= n:
                return 0
            
            # if we don't have a coin, we can choose to buy a coin and then we signal that we're holding a coin OR we can just not buy
            if not holding:
                memo[(i, holding)] = max(-prices[i] + trade(i + 1, True), trade(i + 1))

            # if we do have a coin we're holding, we can choose to sell at the current price and advance to 2 days from now OR we can just advance without selling and just hold.
            else:
                memo[(i, holding)] = max(prices[i] + trade(i + 2, False), trade(i + 1, holding))
            return memo[(i, holding)]


        # when we call, it's presumed that we're not holding or purchased anything and we just started
        return trade(0, False)