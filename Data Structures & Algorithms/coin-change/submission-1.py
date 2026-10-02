class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        # essentially, with the base case of 0, we keep adding 1 until we hit the base case of 0. otherwise, it'll just keep propagating the infinity up. the reason why this works is because we do the minimum repeatedly until we hit. essentially, we're trying to find the perfect remainder. i'll find another video, i don't remember this method but there's a better way.
        def dfs(left):
            if left == 0:
                return 0
            if left in memo:
                return memo[left]
            
            res = 30000
            for coin in coins:
                if left - coin >= 0:
                    res = min(res, 1 + dfs(left - coin))
            
            memo[left] = res
            return res

        least_coins = dfs(amount)
        if least_coins < 30000:
            return least_coins
        return -1
        