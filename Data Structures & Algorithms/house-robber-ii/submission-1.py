class Solution:
    def rob(self, nums: List[int]) -> int:
        # okay, different approach. we can just do the max between 2 intervals. if we do the robber for 0 index all to the n - 1, then we do 1 to n, this means that we avoid the issue with the adjacent ends. the main insight here is that by initializing the memoization in the helper instead of the main function, each localized helper call gets its own memo hashmap. we choose the start and the end, which is either including the start all the way to end - 1, or the start + 1 to the end. this is necessary to enforce the circularity (which really just means we choose the first or the last exclusive).
        # this is the main helper, helps us enforce where we start ane end
        if len(nums) <= 1:
            return nums[0]
        def rob_range(start, end):
            memo = {}
            def act(i):
                # we use end instead of len(nums) or whatever so we can choose the end
                if i >= end:
                    return 0
                # rest of the logic is pretty obvious
                if not memo.get(i):
                    memo[i] = max(nums[i] + act(i + 2), act(i + 1))
                return memo[i]
            return max(nums[start] + act(start + 2), act(start + 1))
        # here's the other part of the insight. we either include the first but not the last or vice versa.
        return max(rob_range(0, len(nums) - 1), rob_range(1, len(nums)))