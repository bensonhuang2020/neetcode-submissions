class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # so the decision is that we want to simplify the decisions that can be taken. for each step, we choose a specific coin right? how to determine that we're not using the same coin?

        # simple, just remember that we can take a coin or not take a coin. i'll just naïvely assume that we can always take a coin until we can't. hence, we take from coin indices until we can't move anymore. instead of doing a for loop, it's probably easier if we choose to take the current coin or if we move to the next
        n = len(coins)
        memo = {}
        def coin(index, target):
            if (index, target) in memo:
                return memo[(index, target)]
            if target == 0:
                return 1
            # if we get to index being greater than n, we can't continue so stop with 0
            if target < 0 or index >= n:
                return 0
            
            # we take the current coin or we move on to the next coin. this keeps going until we hit or go past the target. we also go to the next coin. memo helps reduce duplicate work.
            memo[(index, target)] = coin(index, target - coins[index]) + coin(index + 1, target)

            return memo[(index, target)]
        
        return coin(0, amount)
                
