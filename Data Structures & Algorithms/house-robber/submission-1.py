class Solution:
    def rob(self, nums: List[int]) -> int:
        # this one is simple from bottom up, but essentially, we know that if we're beyond houses, this gives us 0. if we are stealing, we can steal the current and then the one after the adjacent, or we can just do the next house over. the way it works, we can memoize so we don't do dupes. because we can just keep skipping or take the curent best, it doesn't even matter if we took 1 bad route since max helps us reconcile.
        memo = {}
        n = len(nums)

        def dfs(curr):
            if curr >= n:
                return 0
            if not memo.get(curr):
                memo[curr] = max(nums[curr] + dfs(curr + 2), dfs(curr + 1))
            return memo[curr]

        
        return max(nums[0] + dfs(2), dfs(1))