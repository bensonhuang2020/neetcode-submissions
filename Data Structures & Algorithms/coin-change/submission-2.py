class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # the idea is that if we keep an array and we try to calculate the amount of coins upwards, (as in we start with the cheapest coin and we build upwards with the minimization building up)
        amounts = [amount + 1 for value in range(amount + 1)] # we want to contain 0 to amount, and also by making the amount + 1 the initial value, we make each coin unable to contribute to the next unless it's actually makeable.
        amounts[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    amounts[i] = min(amounts[i - coin] + 1, amounts[i])
        
        # then, if the amount buildup is not amount + 1, we know that it actually solved.
        if amounts[amount] == amount + 1:
            return -1
        return amounts[amount]