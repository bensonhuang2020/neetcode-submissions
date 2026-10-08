class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # so the decision is that we want to simplify the decisions that can be taken. for each step, we choose a specific coin right? how to determine that we're not using the same coin?
        n = len(coins)
        memo = {}
        def coin(index, target):
            if (index, target) in memo:
                return memo[(index, target)]
            if target == 0:
                return 1
            if target < 0:
                return 0
            
            for i in range(index, n):
                if (index, target) not in memo:
                    memo[(index, target)] = coin(i, target - coins[i])
                else:
                    memo[(index, target)] += coin(i, target - coins[i])
            return memo[(index, target)]
        
        return coin(0, amount)
                
