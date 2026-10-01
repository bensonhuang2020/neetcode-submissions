class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)

        def dfs(curr):
            if curr >= n:
                return 0
            if not memo.get(curr):
                memo[curr] = max(nums[curr] + dfs(curr + 2), dfs(curr + 1))
            return memo[curr]

        
        return max(nums[0] + dfs(2), dfs(1))