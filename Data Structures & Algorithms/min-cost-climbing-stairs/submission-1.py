class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # memo, take 1 or 2 steps. if we already calculated with 2 steps from the 1 step, then we just take what we already calculated.
        memo = {}
        n = len(cost)
        def climb(i):
            if i >= n:
                return 0
            if not memo.get(i):
                curr = cost[i] + min(climb(i + 1), climb(i + 2))
                memo[i] = curr
            return memo[i]
        return min(climb(0), climb(1))
            